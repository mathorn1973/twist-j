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
        links_.assign(static_cast<std::size_t>(V_) * D, 0);
        if (start == "hot") {
            for (std::size_t i = 0; i < links_.size(); ++i)
                links_[i] = static_cast<std::uint8_t>(rng_.bounded5(0, i));
        }
        flux_.assign(static_cast<std::size_t>(V_) * NPAIR, 0);
        exact_weight_ = {{{4, 0}, {1, 1}, {2, -1}, {2, -1}, {1, 1}}};
        const long double phi = (1.0L + std::sqrt(5.0L)) / 2.0L;
        numeric_weight_ = {
            4.0L,
            phi * phi,
            1.0L / (phi * phi),
            1.0L / (phi * phi),
            phi * phi,
        };
        for (int f = 0; f < 5; ++f) log_weight_[f] = std::log(numeric_weight_[f]);
        recompute_flux();
    }

    int L() const { return L_; }
    int volume() const { return V_; }
    const std::vector<std::array<int, D>> &plus() const { return plus_; }

    void sweep(std::uint64_t sweep_index) {
        const std::uint64_t count = static_cast<std::uint64_t>(V_) * D;
        for (std::uint64_t ordinal = 0; ordinal < count; ++ordinal)
            update_link(static_cast<int>(ordinal / D), static_cast<int>(ordinal % D), sweep_index, ordinal);
    }

    long double mean_log_weight() const {
        long double sum = 0;
        for (std::uint8_t value : flux_) sum += log_weight_[value];
        return sum / static_cast<long double>(flux_.size());
    }

    std::array<int, 5> flux_histogram() const {
        std::array<int, 5> histogram{};
        for (std::uint8_t value : flux_) ++histogram[value];
        return histogram;
    }

    long double score_mean() const {
        const long double g2 = 2.0L + std::sqrt(5.0L);
        const std::array<long double, 5> score{{0.0L, 1.0L, g2, -g2, -1.0L}};
        long double sum = 0;
        for (std::uint8_t value : flux_) sum += score[value];
        return sum / static_cast<long double>(flux_.size());
    }

    std::array<std::complex<long double>, D> polyakov() const {
        const long double pi = std::acos(-1.0L);
        std::array<std::complex<long double>, 5> roots{};
        for (int value = 0; value < 5; ++value)
            roots[value] = std::polar(1.0L, 2.0L * pi * value / 5.0L);
        std::array<std::complex<long double>, D> result{};
        for (int mu = 0; mu < D; ++mu) {
            std::complex<long double> sum{0, 0};
            int count = 0;
            for (int site = 0; site < V_; ++site) {
                if (coords_[site][mu] != 0) continue;
                int phase = 0;
                int cursor = site;
                for (int step = 0; step < L_; ++step) {
                    phase = mod5(phase + links_[static_cast<std::size_t>(cursor) * D + mu]);
                    cursor = plus_[cursor][mu];
                }
                sum += roots[phase];
                ++count;
            }
            result[mu] = sum / static_cast<long double>(count);
        }
        return result;
    }

    ComponentStats vortex_components() const {
        const int nfaces = V_ * NPAIR;
        const int nedges = V_ * D;
        std::vector<std::vector<int>> edge_faces(nedges);
        std::vector<char> occupied(nfaces, 0);
        std::vector<std::array<int, D>> center2(nfaces);
        int occupied_count = 0;
        for (int site = 0; site < V_; ++site) {
            for (int p = 0; p < NPAIR; ++p) {
                const int id = site * NPAIR + p;
                const int a = PAIRS[p][0];
                const int b = PAIRS[p][1];
                center2[id] = {
                    2 * coords_[site][0] + (a == 0) + (b == 0),
                    2 * coords_[site][1] + (a == 1) + (b == 1),
                    2 * coords_[site][2] + (a == 2) + (b == 2),
                    2 * coords_[site][3] + (a == 3) + (b == 3),
                };
                if (flux_[id] == 0) continue;
                occupied[id] = 1;
                ++occupied_count;
                edge_faces[site * D + a].push_back(id);
                edge_faces[plus_[site][a] * D + b].push_back(id);
                edge_faces[plus_[site][b] * D + a].push_back(id);
                edge_faces[site * D + b].push_back(id);
            }
        }
        std::vector<std::vector<int>> adjacency(nfaces);
        for (const auto &faces : edge_faces) {
            for (std::size_t i = 0; i < faces.size(); ++i) {
                for (std::size_t j = i + 1; j < faces.size(); ++j) {
                    adjacency[faces[i]].push_back(faces[j]);
                    adjacency[faces[j]].push_back(faces[i]);
                }
            }
        }
        ComponentStats stats;
        stats.occupied = occupied_count;
        stats.weighted_occupied = occupied_count;
        const int unset = std::numeric_limits<int>::min();
        std::vector<std::array<int, D>> lift(nfaces);
        for (auto &entry : lift) entry.fill(unset);
        std::queue<int> queue;
        for (int root = 0; root < nfaces; ++root) {
            if (!occupied[root] || lift[root][0] != unset) continue;
            ++stats.components;
            lift[root] = center2[root];
            queue.push(root);
            int size = 0;
            bool wraps = false;
            while (!queue.empty()) {
                const int current = queue.front();
                queue.pop();
                ++size;
                for (int next : adjacency[current]) {
                    auto proposed = lift[current];
                    for (int mu = 0; mu < D; ++mu) {
                        int delta = center2[next][mu] - center2[current][mu];
                        if (delta > L_) delta -= 2 * L_;
                        if (delta < -L_) delta += 2 * L_;
                        proposed[mu] += delta;
                    }
                    if (lift[next][0] == unset) {
                        lift[next] = proposed;
                        queue.push(next);
                    } else if (proposed != lift[next]) {
                        wraps = true;
                    }
                }
            }
            stats.largest = std::max(stats.largest, size);
            stats.wraps = stats.wraps || wraps;
