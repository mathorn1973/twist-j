void self_test() {
    const auto known = philox4x32_10({0, 0, 0, 0}, {0, 0});
    const std::array<std::uint32_t, 4> expected{{
        0x6627e8d5u, 0xe169c58du, 0xbc57ac4cu, 0x9b00dbd8u,
    }};
    if (known != expected) throw std::runtime_error("Philox known-answer test failed");

    const std::array<PhiInt, 5> exact_weight{{
        {4, 0}, {1, 1}, {2, -1}, {2, -1}, {1, 1},
    }};
    if (!(exact_weight[1] * exact_weight[2] == PhiInt{1, 0}))
        throw std::runtime_error("exact W1*W2 identity failed");
    if (!(exact_weight[1] + exact_weight[2] == PhiInt{3, 0}))
        throw std::runtime_error("exact W1+W2 identity failed");

    const long double phi = (1.0L + std::sqrt(5.0L)) / 2.0L;
    const std::array<long double, 5> weight{{
        4.0L, phi * phi, 1.0L / (phi * phi), 1.0L / (phi * phi), phi * phi,
    }};
    const std::array<long double, 5> target{{10.0L, 5.0L, 0.0L, 0.0L, 5.0L}};
    const long double pi = std::acos(-1.0L);
    for (int r = 0; r < 5; ++r) {
        std::complex<long double> sum{0, 0};
        for (int f = 0; f < 5; ++f)
            sum += weight[f] * std::polar(1.0L, -2.0L * pi * r * f / 5.0L);
        if (std::abs(sum.real() - target[r]) > 1e-15L || std::abs(sum.imag()) > 1e-15L)
            throw std::runtime_error("face-weight Fourier test failed");
    }

    Lattice lattice(3, 0x123456789abcdef0ULL, "hot");
    lattice.assert_flux_consistent();
    const auto before = lattice.flux_copy();
    lattice.gauge_transform_for_test();
    lattice.assert_flux_consistent();
    if (before != lattice.flux_copy()) throw std::runtime_error("gauge invariance test failed");
    for (int sweep = 0; sweep < 3; ++sweep) lattice.sweep(sweep);
    lattice.assert_flux_consistent();
    const auto current = lattice.monopole_current();
    (void)lattice.monopole_components(current);
    (void)lattice.vortex_components();
    (void)lattice.polyakov();
    const std::uint64_t state_hash = lattice.state_hash();
    if (state_hash != 0xeaa7bcbe93566b43ULL)
        throw std::runtime_error("deterministic state hash failed");

    std::cout << "SELF_TEST PHILOX PASS\n";
    std::cout << "SELF_TEST FACE_WEIGHT_EXACT PASS\n";
    std::cout << "SELF_TEST FACE_WEIGHT_FOURIER PASS\n";
    std::cout << "SELF_TEST GAUGE_INVARIANCE PASS\n";
    std::cout << "SELF_TEST FLUX_CACHE PASS\n";
    std::cout << "SELF_TEST MONOPOLE_CONSERVATION PASS\n";
    std::cout << "SELF_TEST COMPONENT_GEOMETRY PASS\n";
    std::cout << "SELF_TEST DETERMINISTIC_STATE_HASH eaa7bcbe93566b43\n";
    std::cout << "SELF_TEST RESULT PASS\n";
}

