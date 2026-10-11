// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
// Exact rational Dormand-Prince fifth-order tableau. No adaptive controller.
// Coefficients checked against Hairer, dopri5.f, lines 650-676:
// https://www.unige.ch/~hairer/prog/nonstiff/dopri5.f
#pragma once
namespace dp5 {
struct Q {long n,d;};
/* BEGIN_A */
inline constexpr Q A[7][7]={
 {Q{0,1},Q{0,1},Q{0,1},Q{0,1},Q{0,1},Q{0,1},Q{0,1}},
 {Q{1,5},Q{0,1},Q{0,1},Q{0,1},Q{0,1},Q{0,1},Q{0,1}},
 {Q{3,40},Q{9,40},Q{0,1},Q{0,1},Q{0,1},Q{0,1},Q{0,1}},
 {Q{44,45},Q{-56,15},Q{32,9},Q{0,1},Q{0,1},Q{0,1},Q{0,1}},
 {Q{19372,6561},Q{-25360,2187},Q{64448,6561},Q{-212,729},Q{0,1},Q{0,1},Q{0,1}},
 {Q{9017,3168},Q{-355,33},Q{46732,5247},Q{49,176},Q{-5103,18656},Q{0,1},Q{0,1}},
 {Q{35,384},Q{0,1},Q{500,1113},Q{125,192},Q{-2187,6784},Q{11,84},Q{0,1}}
};
/* END_A */
/* BEGIN_B */
inline constexpr Q B[7]={Q{35,384},Q{0,1},Q{500,1113},Q{125,192},Q{-2187,6784},Q{11,84},Q{0,1}};
/* END_B */
/* BEGIN_C */
inline constexpr Q C[7]={Q{0,1},Q{1,5},Q{3,10},Q{4,5},Q{8,9},Q{1,1},Q{1,1}};
/* END_C */
inline double value(Q q){return double(q.n)/double(q.d);}
} // namespace dp5
