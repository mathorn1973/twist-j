        }
        return stats;
    }

    std::vector<std::int8_t> monopole_current() const {
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
                    principal5(flux_[plus_[x][a] * NPAIR + pbc]) - principal5(flux_[x * NPAIR + pbc])
                    - principal5(flux_[plus_[x][b] * NPAIR + pac]) + principal5(flux_[x * NPAIR + pac])
                    + principal5(flux_[plus_[x][c] * NPAIR + pab]) - principal5(flux_[x * NPAIR + pab]);
                if (df % 5 != 0) throw std::runtime_error("monopole current not divisible by five");
                const int value = df / 5;
                if (value < -2 || value > 2) throw std::runtime_error("monopole current outside [-2,2]");
                const int dual_base = minus_[x][missing];
                current[static_cast<std::size_t>(dual_base) * D + missing] =
                    static_cast<std::int8_t>(epsilon * value);
            }
        }
        for (int x = 0; x < V_; ++x) {
            int divergence = 0;
            for (int mu = 0; mu < D; ++mu) {
                divergence += current[static_cast<std::size_t>(x) * D + mu];
                divergence -= current[static_cast<std::size_t>(minus_[x][mu]) * D + mu];
            }
            if (divergence != 0) throw std::runtime_error("monopole current not conserved");
        }
        return current;
    }

    ComponentStats monopole_components(const std::vector<std::int8_t> &current) const {
        struct Arc { int next; int direction; int sign; int edge; };
        std::vector<std::vector<Arc>> adjacency(V_);
        int occupied = 0;
        int weighted = 0;
        for (int x = 0; x < V_; ++x) {
            for (int mu = 0; mu < D; ++mu) {
                const int edge = x * D + mu;
                const int value = current[edge];
                if (value == 0) continue;
                ++occupied;
                weighted += std::abs(value);
                const int y = plus_[x][mu];
                adjacency[x].push_back({y, mu, +1, edge});
                adjacency[y].push_back({x, mu, -1, edge});
            }
        }
        ComponentStats stats;
        stats.occupied = occupied;
        stats.weighted_occupied = weighted;
        const int unset = std::numeric_limits<int>::min();
        std::vector<std::array<int, D>> lift(V_);
        for (auto &entry : lift) entry.fill(unset);
        std::vector<char> edge_seen(static_cast<std::size_t>(V_) * D, 0);
        std::queue<int> queue;
        for (int root = 0; root < V_; ++root) {
            if (adjacency[root].empty() || lift[root][0] != unset) continue;
            ++stats.components;
            lift[root] = coords_[root];
            queue.push(root);
            int edges = 0;
            bool wraps = false;
            while (!queue.empty()) {
                const int vertex = queue.front();
                queue.pop();
                for (const Arc &arc : adjacency[vertex]) {
                    if (!edge_seen[arc.edge]) {
                        edge_seen[arc.edge] = 1;
                        ++edges;
                    }
                    auto proposed = lift[vertex];
                    proposed[arc.direction] += arc.sign;
                    if (lift[arc.next][0] == unset) {
                        lift[arc.next] = proposed;
                        queue.push(arc.next);
                    } else if (proposed != lift[arc.next]) {
                        wraps = true;
                    }
                }
            }
            stats.largest = std::max(stats.largest, edges);
            stats.wraps = stats.wraps || wraps;
        }
        return stats;
    }

    std::complex<long double> plaquette_phase(int site, int pair) const {
        const long double angle = 2.0L * std::acos(-1.0L) * flux_[site * NPAIR + pair] / 5.0L;
        return std::polar(1.0L, angle);
    }

    void gauge_transform_for_test() {
        std::vector<std::uint8_t> gauge(V_);
        for (int x = 0; x < V_; ++x) {
            int value = 0;
            for (int mu = 0; mu < D; ++mu) value += (mu + 1) * coords_[x][mu];
            gauge[x] = static_cast<std::uint8_t>(mod5(value));
        }
        for (int x = 0; x < V_; ++x) {
            for (int mu = 0; mu < D; ++mu) {
                auto &link = links_[static_cast<std::size_t>(x) * D + mu];
                link = static_cast<std::uint8_t>(mod5(link + gauge[plus_[x][mu]] - gauge[x]));
            }
        }
        recompute_flux();
    }

    std::vector<std::uint8_t> flux_copy() const { return flux_; }

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

    void assert_flux_consistent() const {
        std::vector<std::uint8_t> expected(flux_.size());
        for (int x = 0; x < V_; ++x) {
            for (int p = 0; p < NPAIR; ++p) {
                const int a = PAIRS[p][0], b = PAIRS[p][1];
                expected[x * NPAIR + p] = static_cast<std::uint8_t>(mod5(
                    links_[static_cast<std::size_t>(x) * D + a]
                    + links_[static_cast<std::size_t>(plus_[x][a]) * D + b]
                    - links_[static_cast<std::size_t>(plus_[x][b]) * D + a]
                    - links_[static_cast<std::size_t>(x) * D + b]
                ));
            }
        }
        if (expected != flux_) throw std::runtime_error("cached plaquette flux mismatch");
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
