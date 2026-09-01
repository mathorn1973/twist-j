    }

    void recompute_flux() {
        for (int x = 0; x < V_; ++x) {
            for (int p = 0; p < NPAIR; ++p) {
                const int a = PAIRS[p][0], b = PAIRS[p][1];
                flux_[x * NPAIR + p] = static_cast<std::uint8_t>(mod5(
                    links_[static_cast<std::size_t>(x) * D + a]
                    + links_[static_cast<std::size_t>(plus_[x][a]) * D + b]
                    - links_[static_cast<std::size_t>(plus_[x][b]) * D + a]
                    - links_[static_cast<std::size_t>(x) * D + b]
                ));
            }
        }
    }

    std::array<std::tuple<int, int, int>, 6> incident(int site, int mu) const {
        std::array<std::tuple<int, int, int>, 6> result{};
        int cursor = 0;
        for (int nu = 0; nu < D; ++nu) {
            if (nu == mu) continue;
            const int pair = pair_index(mu, nu);
            const int sign_at_site = mu < nu ? +1 : -1;
            result[cursor++] = {site, pair, sign_at_site};
            result[cursor++] = {minus_[site][nu], pair, -sign_at_site};
        }
        return result;
    }

    void update_link(int site, int mu, std::uint64_t sweep_index, std::uint64_t ordinal) {
        const std::size_t link_id = static_cast<std::size_t>(site) * D + mu;
        const int old_value = links_[link_id];
        const auto affected = incident(site, mu);
        std::array<PhiInt, 5> local_weight{};
        PhiInt total{};
        for (int candidate = 0; candidate < 5; ++candidate) {
            const int delta = candidate - old_value;
            PhiInt value{1, 0};
            for (const auto &[base, pair, sign] : affected) {
                const int flux = mod5(flux_[base * NPAIR + pair] + sign * delta);
                value = value * exact_weight_[flux];
            }
            if (sign_phi(value) <= 0) throw std::runtime_error("nonpositive local heat-bath weight");
            local_weight[candidate] = value;
            total = total + value;
        }
        const std::uint64_t counter = sweep_index * static_cast<std::uint64_t>(V_) * D + ordinal;
        const std::uint64_t draw = rng_.u64(1, counter);
        const int256_t scale = int256_t(1) << 64;
        PhiInt cumulative{};
        int selected = 4;
        for (int candidate = 0; candidate < 5; ++candidate) {
            cumulative = cumulative + local_weight[candidate];
            const int256_t difference_a =
                int256_t(cumulative.a) * scale - int256_t(total.a) * draw;
            const int256_t difference_b =
                int256_t(cumulative.b) * scale - int256_t(total.b) * draw;
            if (sign_phi_wide(difference_a, difference_b) > 0) {
                selected = candidate;
                break;
            }
        }
        const int delta = selected - old_value;
        if (delta == 0) return;
        links_[link_id] = static_cast<std::uint8_t>(selected);
        for (const auto &[base, pair, sign] : affected) {
            flux_[base * NPAIR + pair] = static_cast<std::uint8_t>(
                mod5(flux_[base * NPAIR + pair] + sign * delta)
            );
        }
    }

    int L_;
    int V_;
    CounterRng rng_;
    std::vector<std::array<int, D>> coords_;
    std::vector<std::array<int, D>> plus_;
    std::vector<std::array<int, D>> minus_;
    std::vector<std::uint8_t> links_;
    std::vector<std::uint8_t> flux_;
    std::array<PhiInt, 5> exact_weight_{};
    std::array<long double, 5> numeric_weight_{};
    std::array<long double, 5> log_weight_{};
};

struct CorrTerm {
    int direction;
    int pair;
    bool plus;
};

class CorrelatorAccumulator {
  public:
    CorrelatorAccumulator(int max_n, int measurements)
        : max_n_(max_n), measurements_(measurements) {
        for (int rho = 0; rho < D; ++rho) {
            for (int pair = 0; pair < NPAIR; ++pair) {
                const int a = PAIRS[pair][0], b = PAIRS[pair][1];
                if (rho == a || rho == b) longitudinal_.push_back({rho, pair, true});
                else transverse_.push_back({rho, pair, false});
            }
        }
        if (longitudinal_.size() != 12 || transverse_.size() != 12)
            throw std::runtime_error("correlator orientation census failed");
        const std::size_t count = longitudinal_.size() + transverse_.size();
        product_.assign(static_cast<std::size_t>(max_n_ + 1) * count, {});
        left_.assign(product_.size(), {});
        right_.assign(product_.size(), {});
    }

    void add(const Lattice &lattice) {
        std::vector<CorrTerm> all = longitudinal_;
        all.insert(all.end(), transverse_.begin(), transverse_.end());
        const int volume = lattice.volume();
        for (int n = 1; n <= max_n_; ++n) {
            for (std::size_t term_index = 0; term_index < all.size(); ++term_index) {
                const CorrTerm &term = all[term_index];
                std::complex<long double> product_sum{0, 0};
                std::complex<long double> left_sum{0, 0};
                std::complex<long double> right_sum{0, 0};
                for (int x = 0; x < volume; ++x) {
                    int y = x;
                    for (int step = 0; step < n; ++step)
                        y = lattice.plus()[y][term.direction];
                    const auto wx = lattice.plaquette_phase(x, term.pair);
                    const auto wy = lattice.plaquette_phase(y, term.pair);
                    const auto left_value = term.plus ? wx : std::conj(wx);
                    product_sum += left_value * wy;
                    left_sum += left_value;
                    right_sum += wy;
                }
                const std::size_t index =
                    static_cast<std::size_t>(n) * all.size() + term_index;
                product_[index] += product_sum / static_cast<long double>(volume);
                left_[index] += left_sum / static_cast<long double>(volume);
                right_[index] += right_sum / static_cast<long double>(volume);
            }
        }
    }

    std::complex<long double> total(int n) const {
        const std::size_t count = longitudinal_.size() + transverse_.size();
        std::complex<long double> longitudinal{0, 0};
        std::complex<long double> transverse{0, 0};
        for (std::size_t term_index = 0; term_index < count; ++term_index) {
            const std::size_t index = static_cast<std::size_t>(n) * count + term_index;
            const auto mean_product = product_[index] / static_cast<long double>(measurements_);
            const auto mean_left = left_[index] / static_cast<long double>(measurements_);
            const auto mean_right = right_[index] / static_cast<long double>(measurements_);
            const auto connected = mean_product - mean_left * mean_right;
            if (term_index < longitudinal_.size()) longitudinal += connected;
            else transverse += connected;
        }
        longitudinal /= static_cast<long double>(longitudinal_.size());
        transverse /= static_cast<long double>(transverse_.size());
        return longitudinal + transverse;
    }

  private:
    int max_n_;
    int measurements_;
    std::vector<CorrTerm> longitudinal_;
    std::vector<CorrTerm> transverse_;
    std::vector<std::complex<long double>> product_;
    std::vector<std::complex<long double>> left_;
    std::vector<std::complex<long double>> right_;
};

