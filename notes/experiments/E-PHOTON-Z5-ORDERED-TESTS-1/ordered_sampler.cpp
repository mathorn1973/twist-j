// PRE-PIN engineering adapter. No production authorization is implied.
// Upstream retained separately: guarded capacity and duplicate-validation edits.
#define main ordered_upstream_unused_main
#include "kernel64/photon_z5.cpp"
#undef main
#include <filesystem>
#include <fstream>
#include <map>

namespace ordered {
namespace fs = std::filesystem;
struct Config {
    unsigned L;
    std::uint64_t seed;
    std::uint32_t thermal, samples, between;
    std::string start, chain;
    fs::path output;
    bool synthetic;
    bool stream, thermal_sentinels;
};

std::uint64_t decimal(const std::string &s) {
    if (s.empty() || (s.size() > 1 && s[0] == '0'))
        throw std::runtime_error("noncanonical decimal");
    std::uint64_t value = 0;
    for (char c : s) {
        if (c < '0' || c > '9') throw std::runtime_error("nondecimal argument");
        const auto digit = static_cast<unsigned>(c - '0');
        if (value > (UINT64_MAX - digit) / 10)
            throw std::runtime_error("decimal overflow");
        value = value * 10 + digit;
    }
    return value;
}

Config parse(int argc, char **argv) {
    std::map<std::string, std::string> args;
    for (int i = 1; i < argc; i += 2) {
        if (i + 1 == argc || !args.emplace(argv[i], argv[i + 1]).second)
            throw std::runtime_error("missing or duplicate argument");
    }
    const std::array<std::string, 10> names{{
        "--L", "--seed", "--start", "--thermal", "--samples", "--between",
        "--chain", "--output-dir", "--mode", "--t"
    }};
    const auto take_optional = [&](const std::string &name, const std::string &fallback) {
        const auto found = args.find(name);
        if (found == args.end()) return fallback;
        const auto value = found->second;
        args.erase(found);
        return value;
    };
    const auto transport = take_optional("--transport", "files");
    const auto thermal_flag = take_optional("--thermal-sentinels", "0");
    if (transport != "files" && transport != "stream") throw std::runtime_error("invalid transport");
    if (thermal_flag != "0" && thermal_flag != "1") throw std::runtime_error("invalid thermal flag");
    if (args.size() != names.size()) throw std::runtime_error("ten mandatory named options required");
    for (const auto &name : names)
        if (!args.contains(name)) throw std::runtime_error("missing option " + name);
    if (args.at("--t") != "1") throw std::runtime_error("only exact t=1 is admitted");
    const auto L = decimal(args.at("--L"));
    if (L < 2 || L > 64) throw std::runtime_error("state schema requires 2<=L<=64");
    const auto thermal = decimal(args.at("--thermal"));
    const auto samples = decimal(args.at("--samples"));
    const auto between = decimal(args.at("--between"));
    if (thermal > UINT32_MAX || samples > UINT32_MAX
        || between == 0 || between > UINT32_MAX
        || samples * between > UINT32_MAX - thermal)
        throw std::runtime_error("schedule outside upstream uint32 counter range");
    if (samples == 0 && (thermal == 0 || thermal_flag != "1"))
        throw std::runtime_error("zero samples requires positive thermal and thermal-sentinels=1");
    if (transport == "stream" && args.at("--output-dir") != "-")
        throw std::runtime_error("stream transport requires output-dir=- and writes no states to disk");
    const auto &chain = args.at("--chain");
    const auto alnum = [](char c) {
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
    };
    if (chain.empty() || chain.size() > 64 || !alnum(chain.front()))
        throw std::runtime_error("invalid chain identifier");
    for (char c : chain)
        if (!alnum(c) && c != '_' && c != '.' && c != '-')
            throw std::runtime_error("invalid chain identifier");
    const auto &mode = args.at("--mode");
    if (mode != "run" && mode != "synthetic-zero") throw std::runtime_error("invalid mode");
    const auto &start = args.at("--start");
    if (start != "hot" && start != "cold") throw std::runtime_error("invalid start");
    std::uint64_t volume = 1;
    for (unsigned i = 0; i < 4; ++i) volume *= L;
    const auto decisions_per_cycle = 4 * volume + 4 * L * L * L;
    const auto cycles = thermal + samples * between;
    if (cycles > UINT64_MAX / (256 * decisions_per_cycle))
        throw std::runtime_error("schedule can overflow diagnostic total_bits counter");
    if (cycles > UINT64_MAX / (4 * (UINT64_C(1) << 32)))
        throw std::runtime_error("schedule can overflow flat uniform-rejection counter");
    if (mode == "synthetic-zero" && (start != "cold" || thermal != 0 || samples != 1 || between != 1))
        throw std::runtime_error("synthetic-zero requires cold,thermal=0,samples=1,between=1");
    return {static_cast<unsigned>(L), decimal(args.at("--seed")),
            static_cast<std::uint32_t>(thermal), static_cast<std::uint32_t>(samples),
            static_cast<std::uint32_t>(between), start, chain,
            fs::path(args.at("--output-dir")), mode == "synthetic-zero",
            transport == "stream", thermal_flag == "1"};
}

void save(const Config &c, const std::vector<std::uint8_t> &links,
          std::uint64_t sample, std::uint64_t cycles, bool quiet = false) {
    std::uint64_t expected = 4;
    for (unsigned i = 0; i < 4; ++i) expected *= c.L;
    if (links.size() != expected) throw std::runtime_error("link payload census");
    std::ostringstream name;
    name << "sample-" << std::setw(10) << std::setfill('0') << sample << ".state";
    std::ostringstream header;
    header << "TWISTJ_Z5_ORDERED_LINK_STATE_V1\nL=" << c.L << "\nCHAIN=" << c.chain
        << "\nSAMPLE=" << sample << "\nMACROCYCLE=" << cycles << "\nLINKS=";
    const auto prefix = header.str();
    const std::uint64_t bytes = prefix.size() + links.size() + 5; // LF END LF
    const auto path = c.output / name.str();
    std::ofstream file;
    if (c.stream) {
        std::cout << "STATE_BEGIN sample=" << sample << " bytes=" << bytes << '\n';
    } else {
        if (fs::exists(path)) throw std::runtime_error("refusing existing state");
        file.open(path, std::ios::binary | std::ios::out);
        if (!file) throw std::runtime_error("cannot create state");
    }
    std::ostream &out = c.stream ? std::cout : file;
    out << prefix;
    for (auto link : links) {
        if (link > 4) throw std::runtime_error("invalid link residue");
        out.put(static_cast<char>('0' + link));
    }
    out << "\nEND\n";
    if (c.stream) {
        out << "STATE_END sample=" << sample << '\n' << std::flush;
        if (!out) throw std::runtime_error("stream state write failure");
        const auto expected_ack = "ACK " + std::to_string(sample);
        std::string ack;
        for (std::size_t i = 0; i <= expected_ack.size(); ++i) {
            const int ch = std::cin.get();
            if (ch == std::char_traits<char>::eof()) throw std::runtime_error("missing state ACK");
            if (ch == '\n') break;
            ack.push_back(static_cast<char>(ch));
        }
        if (ack != expected_ack || std::cin.fail()) throw std::runtime_error("invalid state ACK");
        return;
    }
    file.close();
    if (!file) throw std::runtime_error("state write or close failure");
    if (quiet) return;
    std::cout << "STATE_FILE sample=" << sample << " macrocycle=" << cycles
              << " path=" << name.str() << " bytes=" << fs::file_size(path) << '\n';
}

int execute(const Config &c) {
    // New output directory owns the complete attempt; no overwrite or resume.
    if (!c.stream && !fs::create_directory(c.output)) throw std::runtime_error("output directory must not exist");
    std::cout << "ORDERED_RUN schema=TWISTJ_Z5_ORDERED_LINK_STATE_V1 L=" << c.L
              << " seed=" << c.seed << " start=" << c.start << " chain=" << c.chain
              << " thermal=" << c.thermal << " samples=" << c.samples
              << " between=" << c.between << " t=1 mode="
              << (c.synthetic ? "synthetic-zero" : "run")
              << " transport=" << (c.stream ? "stream" : "files")
              << " thermal_sentinels=" << (c.thermal_sentinels ? 1 : 0) << '\n';
    if (c.synthetic) {
        std::size_t count = 4;
        for (unsigned i = 0; i < 4; ++i) count *= c.L;
        save(c, std::vector<std::uint8_t>(count, 0), 0, 0);
        std::cout << "UPDATE_DIAGNOSTICS macro_cycles=0 local_decisions=0 line_decisions=0 flat_sheets=0 charge_trials=0\n";
        std::cout << "ORDERED_STATUS SYNTHETIC_ONLY\n";
        return 0;
    }
    Lattice lattice(static_cast<int>(c.L), c.seed, c.start);
    std::uint32_t cycle = 0;
    for (; cycle < c.thermal; ++cycle) {
        KernelAccess::macro_cycle(lattice, cycle);
        if (c.thermal_sentinels) {
            std::cout << "THERMAL_SENTINEL macrocycle=" << (static_cast<std::uint64_t>(cycle) + 1) << '\n';
            print_sample(lattice, cycle);
            std::cout << std::flush;
        }
    }
    for (std::uint32_t sample = 0; sample < c.samples; ++sample) {
        for (std::uint32_t gap = 0; gap < c.between; ++gap)
            KernelAccess::macro_cycle(lattice, cycle++);
        lattice.assert_flux_consistent();
        save(c, lattice.links(), sample, cycle);
        print_sample(lattice, sample);  // unchanged sixteen-sentinel inventory
    }
    const auto &diag = lattice.diagnostics();
    std::cout << "UPDATE_DIAGNOSTICS macro_cycles=" << diag.macro_cycles
              << " local_decisions=" << diag.local_updates
              << " line_decisions=" << diag.line_updates
              << " flat_sheets=" << diag.flat_trials
              << " charge_trials=" << diag.charge_trials << '\n';
    print_diagnostics(diag);
    std::cout << "ORDERED_STATUS GENERATION_COMPLETE_UNCLASSIFIED\n";
    return 0;
}
} // namespace ordered

#ifndef PHITORCH_Z5_CHUNK_WORKER
int main(int argc, char **argv) {
#ifdef _WIN32
    _setmode(_fileno(stdin), _O_BINARY);
    _setmode(_fileno(stdout), _O_BINARY);
    _setmode(_fileno(stderr), _O_BINARY);
#endif
    try {
        if (argc == 2 && std::string(argv[1]) == "--upstream-self-test") {
            self_test();
            return 0;
        }
        return ordered::execute(ordered::parse(argc, argv));
    } catch (const std::exception &error) {
        std::cerr << "ORDERED_STOP " << error.what() << '\n';
        return 2;
    }
}
#endif
