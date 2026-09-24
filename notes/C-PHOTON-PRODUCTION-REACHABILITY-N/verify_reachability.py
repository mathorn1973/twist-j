#!/usr/bin/env python3
"""C-PHOTON-PRODUCTION-REACHABILITY-N verifier (engineering design audit).

NON-CANONICAL. Gaussian lattice Maxwell control on (Z/LZ)^4. Applies the frozen
#757 section 9 Polyakov fit rule and the section 11 correlator target to the
ideal Coulomb phase. numpy is an engineering tool; outputs are rounded.
"""
import numpy as np

BETAS = [(1, 4), (1, 2), (3, 4), (1, 1), (3, 2), (2, 1), (3, 1), (5, 1)]
BAND = [(1, 2), (3, 4), (1, 1), (3, 2), (2, 1)]
LPOL = [12, 16, 24, 32]
WINDOWS = {16: range(2, 5), 24: range(3, 7), 32: range(4, 9)}
NSAMP = 4096
SEED0 = 0x757A0D17
Z99 = 2.5758293035489004
T99_DF2 = 9.924843200918276
RELS = [0.003, 0.01, 0.03, 0.1]


def bval(b):
    return b[0] / b[1]


def bstr(b):
    return f"{b[0]}/{b[1]}" if b[1] != 1 else f"{b[0]}"


def lam3_inv(L):
    k = 2 * np.pi * np.arange(L) / L
    c = 2 - 2 * np.cos(k)
    lam = c[:, None, None] + c[None, :, None] + c[None, None, :]
    inv = np.zeros_like(lam)
    inv[lam > 0] = 1.0 / lam[lam > 0]
    return inv


def green3(L):
    return np.real(np.fft.ifftn(lam3_inv(L)))


def pbar_second_moment(L, beta):
    G = green3(L)
    return float(np.mean(np.exp(-(L / beta) * (G[0, 0, 0] - G))))


def pbar_first_moment(L, beta, seed):
    rng = np.random.Generator(np.random.PCG64(seed))
    h = np.sqrt((L / beta) * lam3_inv(L))
    vals = np.empty(NSAMP)
    m2 = np.empty(NSAMP)
    batch = 64
    for s in range(0, NSAMP, batch):
        xi = rng.standard_normal((batch, L, L, L))
        phi = np.real(np.fft.ifftn(np.fft.fftn(xi, axes=(1, 2, 3)) * h, axes=(1, 2, 3)))
        pb = np.mean(np.exp(1j * phi), axis=(1, 2, 3))
        vals[s:s + batch] = np.abs(pb)
        m2[s:s + batch] = np.abs(pb) ** 2
    return float(vals.mean()), float(vals.std(ddof=1) / np.sqrt(NSAMP)), float(m2.mean()), float(m2.std(ddof=1) / np.sqrt(NSAMP))


def wls(xs, ys, ses):
    X = np.column_stack([np.ones(len(xs)), xs])
    W = np.diag(1.0 / np.asarray(ses) ** 2)
    A = X.T @ W @ X
    cov = np.linalg.inv(A)
    beta_hat = cov @ X.T @ W @ np.asarray(ys)
    return float(beta_hat[0]), float(np.sqrt(cov[0, 0]))


def classify(y0, se, crit):
    lo, hi = y0 - crit * se, y0 + crit * se
    if lo > 0:
        return "POSITIVE_LIMIT"
    if lo <= 0 <= hi:
        return "ZERO_COMPATIBLE"
    return "UNRESOLVED"


def corr_kernels(L):
    k = 2 * np.pi * np.arange(L) / L
    c = 2 - 2 * np.cos(k)
    c0 = c[:, None, None, None]
    c1 = c[None, :, None, None]
    c2 = c[None, None, :, None]
    c3 = c[None, None, None, :]
    lam = c0 + c1 + c2 + c3
    num = (c0 + c1) * np.ones_like(lam)
    frac = np.zeros_like(lam)
    frac[lam > 0] = num[lam > 0] / lam[lam > 0]
    V = L ** 4
    out_long, out_trans = {}, {}
    k0 = k[:, None, None, None]
    k2 = k[None, None, :, None]
    for n in range(0, L // 2 + 1):
        out_long[n] = float(np.sum(np.cos(n * k0) * frac) / V)
        out_trans[n] = float(np.sum(np.cos(n * k2) * frac) / V)
    return out_long, out_trans


def q4(L, n):
    a = n ** -4 + (L - n) ** -4
    b = (n + 1) ** -4 + (L - n - 1) ** -4
    return a / b


def main():
    print("C-PHOTON-PRODUCTION-REACHABILITY-N engineering audit")
    print("control: free lattice Maxwell field on (Z/LZ)^4; no TWIST data")
    # Section A: Green function sanity
    for L in [16, 32, 64]:
        print(f"G3 L={L} G(0)={green3(L)[0,0,0]:.6f}")
    # Section B: Polyakov
    reach = {}
    for bi, b in enumerate(BETAS):
        beta = bval(b)
        R, SE, M2 = [], [], []
        for L in LPOL:
            seed = SEED0 + 1000 * L + bi
            r1, s1, m2s, m2se = pbar_first_moment(L, beta, seed)
            m2e = pbar_second_moment(L, beta)
            R.append(r1)
            SE.append(s1)
            M2.append(m2e)
            print(f"POLY beta={bstr(b)} L={L} R_L={r1:.6e} mcse={s1:.2e} E|P|^2_exact={m2e:.6e} E|P|^2_mc={m2s:.6e} coherent={np.exp(-(L/beta)*green3(L)[0,0,0]):.6e} noise=L^-3={L**-3:.3e}")
        y0 = {}
        for name, xs in (("M1", [1.0 / L for L in LPOL]), ("M2", [1.0 / L ** 2 for L in LPOL])):
            yi, _ = wls(xs, R, [0.01 * r for r in R])
            y0[name] = yi
            cls = []
            for rel in RELS:
                yy, se = wls(xs, R, [rel * r for r in R])
                cls.append(f"r={rel}:z:{classify(yy, se, Z99)}/t2:{classify(yy, se, T99_DF2)}")
            print(f"FIT beta={bstr(b)} {name} intercept={yi:.6e} " + " ".join(cls))
        reach[b] = (y0["M1"] > 0) and (y0["M2"] > 0)
        print(f"POLY_REACHABLE beta={bstr(b)} {reach[b]}")
    band = [reach[b] for b in BAND]
    if not any(band):
        term = "DESIGN_POLYAKOV_UNREACHABLE"
    elif all(band):
        term = "DESIGN_POLYAKOV_REACHABLE"
    else:
        term = "DESIGN_POLYAKOV_BETA_DEPENDENT"
    thr = [bstr(b) for b in BETAS if reach[b]]
    print(f"POLY_REACHABLE_SET {thr}")
    # Section C: correlator target bias at beta = 1 (and beta = 1/2)
    maxbias = 0.0
    for L in [16, 24, 32]:
        kl, kt = corr_kernels(L)
        for beta in (1.0, 0.5):
            s2 = kl[0] / beta
            def C(n):
                return 12 * np.exp(-s2) * (np.exp(-kl[n] / beta) - 1) + 12 * np.exp(-s2) * (np.exp(kt[n] / beta) - 1)
            for n in WINDOWS[L]:
                Q = C(n) / C(n + 1)
                D = Q / q4(L, n) - 1
                if L in (24, 32) and beta == 1.0:
                    maxbias = max(maxbias, abs(D))
                print(f"CORR L={L} beta={beta} n={n} C(n)={C(n):.6e} Klong={kl[n]/beta:.6e} Ktrans={kt[n]/beta:.6e} Q={Q:.6f} Q4={q4(L,n):.6f} D={D:+.5f}")
    sterm = "CORRELATOR_TARGET_BIAS_HIGH" if maxbias > 0.01 else "CORRELATOR_TARGET_BIAS_LOW"
    print(f"MAX_ABS_D_L24_32_beta1 {maxbias:.5f}")
    print(f"TERMINAL {term}")
    print(f"SECONDARY {sterm}")


if __name__ == "__main__":
    main()
