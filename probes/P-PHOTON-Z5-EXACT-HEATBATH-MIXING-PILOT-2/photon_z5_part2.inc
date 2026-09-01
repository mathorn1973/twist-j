
class Lattice {
  public:
    Lattice(int linear_size, std::uint64_t seed, const std::string &start)
        : L_(linear_size), V_(1), rng_(seed) {
        for (int i = 0; i < D; ++i) V_ *= L_;
        coords_.resize(V_);
        plus_.resize(V_);
        minus_.resize(V_);
        for (int site = 0; site < V_; ++site) {
            coords_[site] = decode(site);
            for (int mu = 0; mu < D; ++mu) {
                auto xp = coords_[site];
                auto xm = coords_[site];
                xp[mu] = (xp[mu] + 1) % L_;
                xm[mu] = (xm[mu] + L_ - 1) % L_;
                plus_[site][mu] = encode(xp);
                minus_[site][mu] = encode(xm);
            }
        }
        validate_line_geometry();
        links_.assign(static_cast<std::size_t>(V_) * D, 0);
        if (start == "hot") {
            for (std::uint32_t ordinal = 0; ordinal < links_.size(); ++ordinal) {
                links_[ordinal] = static_cast<std::uint8_t>(exact_uniform5(
                    rng_, RandomKind::HOT, 0, ordinal,
                    diagnostics_.uniform_rejections[kind_slot(RandomKind::HOT)]
                ));
            }
        } else if (start != "cold") {
            throw std::runtime_error("invalid lattice start");
        }
        flux_.assign(static_cast<std::size_t>(V_) * NPAIR, 0);
        recompute_flux();
    }

    int L() const { return L_; }
    int volume() const { return V_; }
    const KernelDiagnostics &diagnostics() const { return diagnostics_; }
    const std::vector<std::uint8_t> &links() const { return links_; }
    const std::vector<std::uint8_t> &flux() const { return flux_; }
    const std::vector<std::array<int, D>> &coordinates() const { return coords_; }

    // TWISTJ_FNVLIKE64_V1 is a fingerprint, not a custody hash: offset
    // 1469598103934665603 (intentionally not standard FNV-1a's trailing-7
    // offset), prime 1099511628211, xor/multiply per uint8 modulo 2^64.
    // State absorbs links then cached flux; cache hash absorbs flux only.
    // Logs render both as exactly sixteen lowercase hexadecimal digits.
    std::uint64_t state_hash() const {
        std::uint64_t hash = 1469598103934665603ULL;
        auto absorb = [&](std::uint8_t value) {
            hash ^= value;
            hash *= 1099511628211ULL;
        };
        for (std::uint8_t value : links_) absorb(value);
        for (std::uint8_t value : flux_) absorb(value);
        return hash;
    }

    std::uint64_t flux_cache_hash() const {
        std::uint64_t hash = 1469598103934665603ULL;
        for (std::uint8_t value : flux_) {
            hash ^= value;
            hash *= 1099511628211ULL;
        }
        return hash;
    }

    std::array<std::uint64_t, 5> flux_histogram() const {
        std::array<std::uint64_t, 5> histogram{};
        for (std::uint8_t value : flux_) ++histogram[value];
        return histogram;
    }

    long double mean_log_weight() const {
        const long double phi = (1.0L + std::sqrt(5.0L)) / 2.0L;
        const std::array<long double, 5> numeric{{
            4.0L, phi * phi, 1.0L / (phi * phi), 1.0L / (phi * phi), phi * phi,
        }};
        long double sum = 0;
        for (std::uint8_t value : flux_) sum += std::log(numeric[value]);
        return sum / static_cast<long double>(flux_.size());
    }

    long double score_mean() const {
        const long double g2 = 2.0L + std::sqrt(5.0L);
        const std::array<long double, 5> score{{0.0L, 1.0L, g2, -g2, -1.0L}};
        long double sum = 0;
        for (std::uint8_t value : flux_) sum += score[value];
        return sum / static_cast<long double>(flux_.size());
    }

    std::array<long double, D> polyakov_radii() const {
        const long double pi = std::acos(-1.0L);
        std::array<std::complex<long double>, 5> roots{};
        for (int value = 0; value < 5; ++value)
            roots[value] = std::polar(1.0L, 2.0L * pi * value / 5.0L);
        std::array<long double, D> result{};
        for (int mu = 0; mu < D; ++mu) {
            std::complex<long double> sum{0, 0};
            std::uint64_t count = 0;
            for (int base = 0; base < V_; ++base) {
                if (coords_[base][mu] != 0) continue;
                int phase = 0;
                int site = base;
                for (int step = 0; step < L_; ++step) {
                    phase = mod5(phase + links_[static_cast<std::size_t>(site) * D + mu]);
                    site = plus_[site][mu];
                }
                sum += roots[phase];
                ++count;
            }
            result[mu] = std::abs(sum / static_cast<long double>(count));
        }
        return result;
    }

    long double vortex_density() const {
        std::uint64_t occupied = 0;
        for (std::uint8_t value : flux_) if (value != 0) ++occupied;
        return static_cast<long double>(occupied) / static_cast<long double>(flux_.size());
    }

    long double monopole_density() const {
        std::vector<std::int8_t> current(static_cast<std::size_t>(V_) * D, 0);
        for (int missing = 0; missing < D; ++missing) {
            std::array<int, 3> axes{};
            int cursor = 0;
            for (int mu = 0; mu < D; ++mu)
                if (mu != missing) axes[cursor++] = mu;
            const int a = axes[0], b = axes[1], c = axes[2];
            const int pbc = pair_index(b, c);
            const int pac = pair_index(a, c);
            const int pab = pair_index(a, b);
            const int epsilon = (missing % 2 == 0) ? 1 : -1;
            for (int x = 0; x < V_; ++x) {
                const int df =
                    principal5(flux_[static_cast<std::size_t>(plus_[x][a]) * NPAIR + pbc])
                    - principal5(flux_[static_cast<std::size_t>(x) * NPAIR + pbc])
                    - principal5(flux_[static_cast<std::size_t>(plus_[x][b]) * NPAIR + pac])
                    + principal5(flux_[static_cast<std::size_t>(x) * NPAIR + pac])
                    + principal5(flux_[static_cast<std::size_t>(plus_[x][c]) * NPAIR + pab])
                    - principal5(flux_[static_cast<std::size_t>(x) * NPAIR + pab]);
                if (df % 5 != 0)
                    throw StopIntegrity("STOP_INTEGRITY monopole_current_not_divisible_by_five");
                const int value = epsilon * (df / 5);
                if (value < -2 || value > 2)
                    throw StopIntegrity("STOP_INTEGRITY monopole_current_outside_range");
                current[static_cast<std::size_t>(minus_[x][missing]) * D + missing] =
                    static_cast<std::int8_t>(value);
            }
        }
        std::uint64_t occupied = 0;
        for (int x = 0; x < V_; ++x) {
            int divergence = 0;
            for (int mu = 0; mu < D; ++mu) {
                const int value = current[static_cast<std::size_t>(x) * D + mu];
                divergence += value;
                divergence -= current[static_cast<std::size_t>(minus_[x][mu]) * D + mu];
                if (value != 0) ++occupied;
            }
            if (divergence != 0)
                throw StopIntegrity("STOP_INTEGRITY monopole_current_not_conserved");
        }
        return static_cast<long double>(occupied)
            / static_cast<long double>(static_cast<std::uint64_t>(V_) * D);
    }

    std::vector<std::uint8_t> computed_flux() const {
        std::vector<std::uint8_t> result(static_cast<std::size_t>(V_) * NPAIR);
        for (int x = 0; x < V_; ++x) {
            for (int p = 0; p < NPAIR; ++p) {
                const int a = PAIRS[p][0];
                const int b = PAIRS[p][1];
                result[static_cast<std::size_t>(x) * NPAIR + p] = static_cast<std::uint8_t>(mod5(
                    links_[static_cast<std::size_t>(x) * D + a]
                    + links_[static_cast<std::size_t>(plus_[x][a]) * D + b]
                    - links_[static_cast<std::size_t>(plus_[x][b]) * D + a]
                    - links_[static_cast<std::size_t>(x) * D + b]
                ));
            }
        }
        return result;
    }

    void assert_flux_consistent() const {
        if (computed_flux() != flux_)
            throw StopIntegrity("STOP_INTEGRITY cached_plaquette_flux_mismatch");
    }

    void gauge_transform_for_test() {
        const auto before = flux_;
        std::vector<std::uint8_t> gauge(V_);
        for (int x = 0; x < V_; ++x) {
            int value = 0;
            for (int mu = 0; mu < D; ++mu) value += (mu + 1) * coords_[x][mu];
            gauge[x] = static_cast<std::uint8_t>(mod5(value));
        }
        for (int x = 0; x < V_; ++x) {
            for (int mu = 0; mu < D; ++mu) {
                auto &link = links_[static_cast<std::size_t>(x) * D + mu];
                link = static_cast<std::uint8_t>(mod5(
                    link + gauge[plus_[x][mu]] - gauge[x]
                ));
            }
        }
        recompute_flux();
        if (flux_ != before) throw std::runtime_error("gauge transformation changed flux");
    }

    QPhi global_weight() const {
        QPhi result{1, 0};
        for (std::uint8_t value : flux_) result = result * face_weights()[value];
        if (sign_qphi(result) <= 0) throw std::runtime_error("nonpositive global weight");
        return result;
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

    const std::array<QPhi, 5> &local_masses(int site, int mu) const {
        const std::size_t link_id = static_cast<std::size_t>(site) * D + mu;
        const int old_value = links_[link_id];
        const auto affected = incident(site, mu);
        std::array<int, 3> positive{};
        std::array<int, 3> negative{};
        int positive_count = 0, negative_count = 0;
        for (const auto &[base, pair, sign] : affected) {
            const int residual = mod5(
                flux_[static_cast<std::size_t>(base) * NPAIR + pair] - sign * old_value
            );
            if (sign > 0) positive[positive_count++] = residual;
            else negative[negative_count++] = residual;
        }
        if (positive_count != 3 || negative_count != 3)
            throw StopIntegrity("STOP_INTEGRITY local_incidence_sign_census_failed");
        int key = 0;
        for (int residual : positive) key = 5 * key + residual;
        for (int residual : negative) key = 5 * key + residual;
        return local_mass_table()[key];
    }

    void local_sweep(std::uint32_t cycle, bool reverse) {
        const std::uint32_t count = static_cast<std::uint32_t>(links_.size());
        if (reverse) ++diagnostics_.local_reverse_sweeps;
        else ++diagnostics_.local_forward_sweeps;
        for (std::uint32_t step = 0; step < count; ++step) {
            const std::uint32_t link_id = reverse ? count - 1 - step : step;
            update_link(link_id, cycle);
        }
    }

    void apply_link_value_for_test(int site, int mu, int selected) {
        const std::size_t link_id = static_cast<std::size_t>(site) * D + mu;
        const int delta = selected - links_[link_id];
        links_[link_id] = static_cast<std::uint8_t>(mod5(selected));
        for (const auto &[base, pair, sign] : incident(site, mu)) {
            auto &value = flux_[static_cast<std::size_t>(base) * NPAIR + pair];
            value = static_cast<std::uint8_t>(mod5(value + sign * delta));
        }
    }

    void apply_flat_sheet_for_test(int mu, int shift) {
        const auto cache_before = flux_;
        for (int site = 0; site < V_; ++site) {
            if (coords_[site][mu] != 0) continue;
            auto &link = links_[static_cast<std::size_t>(site) * D + mu];
            link = static_cast<std::uint8_t>(mod5(link + shift));
        }
        if (flux_ != cache_before || computed_flux() != flux_)
            throw std::runtime_error("fixed flat-sheet test failed");
    }

    void apply_charge_for_test() {
        const QPhi before = global_weight();
        for (auto &link : links_) link = static_cast<std::uint8_t>(mod5(-link));
        for (auto &value : flux_) value = static_cast<std::uint8_t>(mod5(-value));
        if (computed_flux() != flux_ || !(global_weight() == before))
            throw std::runtime_error("fixed charge-conjugation identity failed");
    }

  private:
    std::array<int, D> decode(int site) const {
        std::array<int, D> result{};
        for (int mu = D - 1; mu >= 0; --mu) {
            result[mu] = site % L_;
            site /= L_;
        }
        return result;
    }

    int encode(const std::array<int, D> &coordinate) const {
        int site = 0;
        for (int mu = 0; mu < D; ++mu) site = site * L_ + coordinate[mu];
        return site;
    }

    void recompute_flux() { flux_ = computed_flux(); }

    void update_link(std::uint32_t link_id, std::uint32_t cycle) {
        const int site = static_cast<int>(link_id / D);
        const int mu = static_cast<int>(link_id % D);
        const int old_value = links_[link_id];
        const auto &masses = local_masses(site, mu);
        CounterBits bits(rng_, RandomKind::LOCAL, cycle, link_id);
        const int selected = exact_category(
            masses,
            bits,
            diagnostics_.sampler[kind_slot(RandomKind::LOCAL)]
        );
        ++diagnostics_.local_updates;
        const int delta = selected - old_value;
        if (delta == 0) return;
        ++diagnostics_.local_changes;
        links_[link_id] = static_cast<std::uint8_t>(selected);
        for (const auto &[base, pair, sign] : incident(site, mu)) {
            auto &value = flux_[static_cast<std::size_t>(base) * NPAIR + pair];
            value = static_cast<std::uint8_t>(mod5(value + sign * delta));
        }
    }

  public:
    // The following exact orbit operations are public only so the integrity
    // self-test can compare the local orbit mass to the complete action.
    struct LineFace { std::size_t id{0}; int sign{0}; };
    struct LineFaces {
        std::array<LineFace, 6 * 16> entries{};
        std::size_t count{0};
        const LineFace *begin() const { return entries.data(); }
        const LineFace *end() const { return entries.data() + count; }
    };

    LineFaces line_faces(int base, int mu) const {
        if (coords_[base][mu] != 0)
            throw StopIntegrity("STOP_INTEGRITY invalid_noncontractible_line_base");
        LineFaces result;
        int site = base;
        for (int step = 0; step < L_; ++step) {
            for (const auto &[face_base, pair, sign] : incident(site, mu))
                result.entries[result.count++] = {
                    static_cast<std::size_t>(face_base) * NPAIR + pair, sign
                };
            site = plus_[site][mu];
        }
        if (result.count != static_cast<std::size_t>(6 * L_))
            throw StopIntegrity("STOP_INTEGRITY noncontractible_line_face_census_failed");
        return result;
    }

    std::array<QPhi, 5> line_masses(int base, int mu) const {
        return line_masses(line_faces(base, mu));
    }

    std::array<QPhi, 5> line_masses(const LineFaces &affected) const {
        std::array<QPhi, 5> masses{};
        for (int delta = 0; delta < 5; ++delta) {
            std::array<unsigned, 5> counts{};
            for (const LineFace &entry : affected) {
                const int value = mod5(flux_[entry.id] + entry.sign * delta);
                ++counts[value];
            }
            QPhi mass{1, 0};
            // Exact count/power accumulation avoids 5 x 6L repeated products.
            for (int value = 0; value < 5; ++value) {
                QPhi base_weight = face_weights()[value];
                unsigned exponent = counts[value];
                while (exponent != 0) {
                    if (exponent & 1u) mass = mass * base_weight;
                    exponent >>= 1u;
                    if (exponent != 0) base_weight = base_weight * base_weight;
                }
            }
            if (sign_qphi(mass) <= 0)
                throw StopIntegrity("STOP_INTEGRITY nonpositive_line_heatbath_mass");
            masses[delta] = mass;
        }
        return masses;
    }

    void apply_line_delta_for_test(int base, int mu, int delta) {
        const LineFaces affected = line_faces(base, mu);
        apply_line_delta(base, mu, delta, affected);
    }

  private:
    void apply_line_delta(int base, int mu, int delta, const LineFaces &affected) {
        delta = mod5(delta);
        if (delta == 0) return;
        int site = base;
        for (int step = 0; step < L_; ++step) {
            auto &link = links_[static_cast<std::size_t>(site) * D + mu];
            link = static_cast<std::uint8_t>(mod5(link + delta));
            site = plus_[site][mu];
        }
        for (const LineFace &entry : affected) {
            auto &value = flux_[entry.id];
            value = static_cast<std::uint8_t>(mod5(value + entry.sign * delta));
        }
    }

    void validate_line_geometry() const {
        std::uint64_t lines = 0;
        for (int mu = 0; mu < D; ++mu) {
            for (int base = 0; base < V_; ++base) {
                if (coords_[base][mu] != 0) continue;
                const LineFaces affected = line_faces(base, mu);
                for (std::size_t i = 0; i < affected.count; ++i) {
                    for (std::size_t j = i + 1; j < affected.count; ++j) {
                        if (affected.entries[i].id == affected.entries[j].id)
                            throw StopIntegrity("STOP_INTEGRITY duplicate_noncontractible_line_face");
                    }
                }
                ++lines;
            }
        }
        const std::uint64_t expected = static_cast<std::uint64_t>(D) * L_ * L_ * L_;
        if (lines != expected) throw StopIntegrity("STOP_INTEGRITY constructor_line_census_failed");
    }

    int L_;
    int V_;
    CounterRng rng_;
    KernelDiagnostics diagnostics_;
    std::vector<std::array<int, D>> coords_;
    std::vector<std::array<int, D>> plus_;
    std::vector<std::array<int, D>> minus_;
    std::vector<std::uint8_t> links_;
    std::vector<std::uint8_t> flux_;

    friend class KernelAccess;
};
