// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
#pragma once
#include <array>
#include <string>
#include <vector>
namespace vm {
constexpr int MAX_L=12, MAX_G=16;
struct I { double lo=0, hi=0; };
struct Z { I re, im; };
struct Node {
 I u, cs[2], sn[2], mean[2], k2[2], gaussian[2], beta_norm[2];
 int active[2]{};
 Z beta[2][7], phase[2];
};
struct Cell {
 I h;
 std::array<Node,7> stage;
 std::array<Node,16> gauss;
 std::array<I,16> x,w;
 I h_rho;
 double rho=6;
};
struct Linear { Z alpha[7]; I phase; };
struct Prepared {
 std::array<std::vector<Cell>,6> cells;
 std::array<Linear,6> final;
 std::array<Z,6> linear_pair, rotation;
 std::array<std::array<Z,7>,6> delta;
 std::array<I,6> delta_gaussian, delta_norm;
 std::array<I,120> thermal;
 I thermal_tail, legacy_eta_mismatch;
 std::array<std::array<I,MAX_L+1>,2> tail;
 std::array<I,MAX_G+2> sqrt_n;
 double preparation_seconds=0;
 std::string mpfr_version;
};
// Exact input uses decimal tokens. Every derived quantity is enclosed with
// 192-bit MPFR directed arithmetic before outward conversion to binary64.
Prepared prepare(const std::string& path,int cutoff,int guard,int steps);
}
