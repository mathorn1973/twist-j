#!/usr/bin/env python3
"""Break check for C-PHOTON-PRODUCTION-REACHABILITY-N (independent code paths).

B1 E|Pbar|^2: direct real-space double sum over x,y with G from explicit
   k-sums (no FFT), L = 6, 8, against the FFT formula of the verifier.
B2 G_L(0) large-L trend against the Watson value W3/2 = 0.2527310098.
B3 plaquette covariance in REAL SPACE from the 4D link Green function in
   Feynman gauge, <F01(0)F01(n e_rho)> as a sum of 16 link-link terms,
   against the Fourier formula (|a_0|^2+|a_1|^2)/lambda, L = 8, 16.
B4 Monte Carlo of the Gaussian link field (exact FFT sampler, L = 8):
   C+ and C- estimated directly as E[W W] - E W E W with W = exp(iF),
   against exp(-s2)(exp(-/+K) - 1).
B5 continuum approach: K_long(n) L=64 against -4/(4 pi^2 n^4), and the
   ratio deviation D(n) against a c/n^2 law.
"""
import numpy as np
import math

np.set_printoptions(precision=6)


def green3_direct(L):
    ks = [2 * math.pi * j / L for j in range(L)]
    G = np.zeros((L, L, L))
    kk = []
    for a in ks:
        for b in ks:
            for c in ks:
                lam = 6 - 2 * math.cos(a) - 2 * math.cos(b) - 2 * math.cos(c)
                if lam > 1e-12:
                    kk.append((a, b, c, 1.0 / lam))
    for x in range(L):
        for y in range(L):
            for z in range(L):
                s = 0.0
                for a, b, c, il in kk:
                    s += math.cos(a * x + b * y + c * z) * il
                G[x, y, z] = s / L ** 3
    return G


def green3_fft(L):
    k = 2 * np.pi * np.arange(L) / L
    c = 2 - 2 * np.cos(k)
    lam = c[:, None, None] + c[None, :, None] + c[None, None, :]
    inv = np.zeros_like(lam)
    inv[lam > 0] = 1 / lam[lam > 0]
    return np.real(np.fft.ifftn(inv))


def b1():
    for L in (6, 8):
        Gd = green3_direct(L)
        Gf = green3_fft(L)
        for beta in (0.5, 1.0):
            # direct double sum over x, y
            s = 0.0
            pts = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
            for p in pts:
                for q in pts:
                    r = tuple((p[i] - q[i]) % L for i in range(3))
                    s += math.exp(-(L / beta) * (Gd[0, 0, 0] - Gd[r]))
            direct = s / L ** 6
            fftv = float(np.mean(np.exp(-(L / beta) * (Gf[0, 0, 0] - Gf))))
            print(f"B1 L={L} beta={beta} direct={direct:.12e} fft={fftv:.12e} rel={abs(direct-fftv)/fftv:.2e}")


def b2():
    for L in (32, 64, 128):
        g0 = green3_fft(L)[0, 0, 0]
        print(f"B2 L={L} G(0)={g0:.8f} Watson-G(0)={0.2527310098-g0:.6f} L*(diff)={L*(0.2527310098-g0):.5f}")


def green4_fft(L):
    k = 2 * np.pi * np.arange(L) / L
    c = 2 - 2 * np.cos(k)
    lam = c[:, None, None, None] + c[None, :, None, None] + c[None, None, :, None] + c[None, None, None, :]
    inv = np.zeros_like(lam)
    inv[lam > 0] = 1 / lam[lam > 0]
    return np.real(np.fft.ifftn(inv))


def fourier_K(L, n, rho):
    k = 2 * np.pi * np.arange(L) / L
    c = 2 - 2 * np.cos(k)
    C = [c[:, None, None, None], c[None, :, None, None], c[None, None, :, None], c[None, None, None, :]]
    K = [k[:, None, None, None], k[None, :, None, None], k[None, None, :, None], k[None, None, None, :]]
    lam = C[0] + C[1] + C[2] + C[3]
    num = (C[0] + C[1]) * np.ones_like(lam)
    fr = np.zeros_like(lam)
    fr[lam > 0] = num[lam > 0] / lam[lam > 0]
    return float(np.sum(np.cos(n * K[rho]) * fr) / L ** 4)


def b3():
    for L in (8, 16):
        G = green4_fft(L)
        e = [np.array(v) for v in ([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1])]

        def g(v):
            return G[tuple(int(t) % L for t in v)]
        # F01(x) = A0(x) + A1(x+e0) - A0(x+e1) - A1(x)
        terms = [(0, e[0] * 0, +1), (1, e[0], +1), (0, e[1], -1), (1, e[0] * 0, -1)]
        for rho in (0, 2):
            for n in range(1, 4):
                X = n * e[rho]
                s = 0.0
                for (mu, u, su) in terms:
                    for (nu, v, sv) in terms:
                        if mu == nu:
                            s += su * sv * g(X + v - u)
                kf = fourier_K(L, n, rho)
                print(f"B3 L={L} rho={rho} n={n} realspace={s:.12e} fourier={kf:.12e} diff={abs(s-kf):.1e}")


def b4():
    L = 8
    beta = 1.0
    rng = np.random.Generator(np.random.PCG64(20260922))
    k = 2 * np.pi * np.arange(L) / L
    c = 2 - 2 * np.cos(k)
    lam = c[:, None, None, None] + c[None, :, None, None] + c[None, None, :, None] + c[None, None, None, :]
    h = np.zeros_like(lam)
    h[lam > 0] = np.sqrt(1 / (beta * lam[lam > 0]))
    nsamp = 4000
    acc = {}
    for _ in range(nsamp):
        A = [np.real(np.fft.ifftn(np.fft.fftn(rng.standard_normal((L, L, L, L))) * h)) for _ in range(4)]
        F01 = A[0] + np.roll(A[1], -1, axis=0) - np.roll(A[0], -1, axis=1) - A[1]
        W = np.exp(1j * F01)
        for rho, lab in ((0, "long"), (2, "trans")):
            for n in (1, 2):
                Wy = np.roll(W, -n, axis=rho)
                prod = np.mean(W * Wy) if lab == "long" else np.mean(np.conj(W) * Wy)
                left = np.mean(W) if lab == "long" else np.mean(np.conj(W))
                right = np.mean(Wy)
                acc.setdefault((lab, n), [0, 0, 0])
                a = acc[(lab, n)]
                a[0] += prod
                a[1] += left
                a[2] += right
    s2 = fourier_K(L, 0, 0) / beta
    for (lab, n), a in sorted(acc.items()):
        est = a[0] / nsamp - (a[1] / nsamp) * (a[2] / nsamp)
        K = fourier_K(L, n, 0 if lab == "long" else 2) / beta
        th = math.exp(-s2) * (math.exp(-K) - 1) if lab == "long" else math.exp(-s2) * (math.exp(K) - 1)
        print(f"B4 L={L} {lab} n={n} MC={est.real:+.5e} (imag {est.imag:+.1e}) theory={th:+.5e}")


def b5():
    L = 64
    k = 2 * np.pi * np.arange(L) / L
    c = 2 - 2 * np.cos(k)
    lam = c[:, None, None, None] + c[None, :, None, None] + c[None, None, :, None] + c[None, None, None, :]
    num = (c[:, None, None, None] + c[None, :, None, None]) * np.ones_like(lam)
    fr = np.zeros_like(lam)
    fr[lam > 0] = num[lam > 0] / lam[lam > 0]
    k0 = k[:, None, None, None]
    prev = None
    for n in range(2, 17):
        Kl = float(np.sum(np.cos(n * k0) * fr) / L ** 4)
        cont = -4 / (4 * math.pi ** 2 * n ** 4)
        print(f"B5 L=64 n={n} K_long={Kl:.6e} continuum={cont:.6e} ratio={Kl/cont:.5f} (ratio-1)*n^2={(Kl/cont-1)*n*n:.4f}")


if __name__ == "__main__":
    b1()
    b2()
    b3()
    b4()
    b5()
