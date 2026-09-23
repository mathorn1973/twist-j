/* zlgt2.c : v2 of the independent Z_N lattice gauge heat-bath engine for
 * C-PHOTON-PHASE-ORIENTATION-N (NON-CANONICAL, engineering orientation).
 * 4D periodic (Z/LZ)^4, arbitrary symmetric plaquette weight table W[0..N-1].
 * Floating point categorical draws (xoshiro256**); no exact-arithmetic claim.
 *
 * usage: zlgt2 N L seed start(cold|hot) ntherm nmeas every corr_every W0..W{N-1} X0..X{N-1}
 *
 * Output lines:
 *   RUN  ...parameters...
 *   M    one line per measurement (see printf in measure())
 *   C    correlator ingredients (every corr_every-th measurement, if > 0)
 *   END  final state hash
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static int N, L, V;
static uint8_t *U;               /* U[x*4+mu] */
static int *nbp, *nbm;           /* neighbours */
static uint8_t *crd;             /* crd[x*4+mu] coordinate */
static double Wt[64], logWt[64], Xt[64], cosT[64], sinT[64];
static double *R;                /* rolled table R[s*N+u] = W[(u+s) mod N] */

static uint64_t s4[4];
static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static inline uint64_t next64(void) {
    const uint64_t result = rotl(s4[1] * 5, 7) * 9;
    const uint64_t t = s4[1] << 17;
    s4[2] ^= s4[0]; s4[3] ^= s4[1]; s4[1] ^= s4[2]; s4[0] ^= s4[3]; s4[2] ^= t; s4[3] = rotl(s4[3], 45);
    return result;
}
static inline double urand(void) { return (next64() >> 11) * 0x1.0p-53; }
static void seedrng(uint64_t seed) {
    uint64_t z = seed;
    for (int i = 0; i < 4; i++) {
        z += 0x9e3779b97f4a7c15ULL;
        uint64_t y = z;
        y = (y ^ (y >> 30)) * 0xbf58476d1ce4e5b9ULL;
        y = (y ^ (y >> 27)) * 0x94d049bb133111ebULL;
        s4[i] = y ^ (y >> 31);
    }
}
static inline int md(int a) { a %= N; return a < 0 ? a + N : a; }

static void geometry(void) {
    V = L * L * L * L;
    nbp = malloc(sizeof(int) * V * 4);
    nbm = malloc(sizeof(int) * V * 4);
    crd = malloc((size_t)V * 4);
    for (int x = 0; x < V; x++) {
        int c[4], t = x;
        for (int mu = 3; mu >= 0; mu--) { c[mu] = t % L; t /= L; }
        for (int mu = 0; mu < 4; mu++) {
            crd[x * 4 + mu] = (uint8_t)c[mu];
            int cp[4], cm[4];
            memcpy(cp, c, sizeof c); memcpy(cm, c, sizeof c);
            cp[mu] = (c[mu] + 1) % L; cm[mu] = (c[mu] + L - 1) % L;
            nbp[x * 4 + mu] = ((cp[0] * L + cp[1]) * L + cp[2]) * L + cp[3];
            nbm[x * 4 + mu] = ((cm[0] * L + cm[1]) * L + cm[2]) * L + cm[3];
        }
    }
}

static void build_table(void) {
    for (int s = 0; s < N; s++)
        for (int u = 0; u < N; u++) R[s * N + u] = Wt[(u + s) % N];
}

static inline int plaq(int x, int mu, int nu) {
    return md(U[x * 4 + mu] + U[nbp[x * 4 + mu] * 4 + nu] - U[nbp[x * 4 + nu] * 4 + mu] - U[x * 4 + nu]);
}

static void sweep(void) {
    double p[64];
    for (int x = 0; x < V; x++) {
        for (int mu = 0; mu < 4; mu++) {
            const double *row[6];
            int k = 0;
            int xpmu = nbp[x * 4 + mu];
            for (int nu = 0; nu < 4; nu++) {
                if (nu == mu) continue;
                int xpnu = nbp[x * 4 + nu], xmnu = nbm[x * 4 + nu];
                int s1 = U[xpmu * 4 + nu] - U[xpnu * 4 + mu] - U[x * 4 + nu];      /* f = u + s1 */
                int s2 = U[xmnu * 4 + mu] + U[nbp[xmnu * 4 + mu] * 4 + nu] - U[xmnu * 4 + nu]; /* f = s2 - u */
                row[k++] = R + md(s1) * N;
                row[k++] = R + md(-s2) * N;   /* W(s2-u) = W(u-s2) by symmetry */
            }
            double tot = 0;
            for (int u = 0; u < N; u++) {
                double w = row[0][u] * row[1][u] * row[2][u] * row[3][u] * row[4][u] * row[5][u];
                p[u] = w; tot += w;
            }
            double r = urand() * tot, c = 0;
            int pick = N - 1;
            for (int u = 0; u < N; u++) { c += p[u]; if (r < c) { pick = u; break; } }
            U[x * 4 + mu] = (uint8_t)pick;
        }
    }
}

static const int PL[6][2] = {{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
static int PIDX[4][4];

static uint8_t *F;
static double *marg;   /* marg[(a*4+mu)*L + k] */

static void measure(long sweepno, int docorr) {
    int half = N / 2;
    double sumcos = 0, sumlogw = 0, sumx2 = 0;
    memset(marg, 0, sizeof(double) * 6 * 4 * L);
    for (int x = 0; x < V; x++) {
        const uint8_t *cx = crd + x * 4;
        for (int a = 0; a < 6; a++) {
            int f = plaq(x, PL[a][0], PL[a][1]);
            F[x * 6 + a] = (uint8_t)f;
            double xv = Xt[f];
            sumcos += cosT[f]; sumlogw += logWt[f]; sumx2 += xv * xv;
            for (int mu = 0; mu < 4; mu++) marg[(a * 4 + mu) * L + cx[mu]] += xv;
        }
    }
    double A[2] = {0, 0}, B[2] = {0, 0};
    for (int a = 0; a < 6; a++)
        for (int mu = 0; mu < 4; mu++)
            for (int m = 1; m <= 2; m++) {
                double re = 0, im = 0;
                for (int k = 0; k < L; k++) {
                    double ph = 2 * M_PI * m * k / L, v = marg[(a * 4 + mu) * L + k];
                    re += v * cos(ph); im -= v * sin(ph);
                }
                double pw = (re * re + im * im) / V;
                int contains = (PL[a][0] == mu || PL[a][1] == mu);
                if (contains) A[m - 1] += pw / 12.0; else B[m - 1] += pw / 12.0;
            }
    /* monopoles on 3-cubes (i<j<k), principal integer lift of F */
    long nmono = 0, mabs = 0;
    static const int CU[4][3] = {{0,1,2},{0,1,3},{0,2,3},{1,2,3}};
#define PR(v) ((int)(v) > half ? (int)(v) - N : (int)(v))
    for (int x = 0; x < V; x++) {
        for (int c = 0; c < 4; c++) {
            int i = CU[c][0], j = CU[c][1], k = CU[c][2];
            int ij = PIDX[i][j], ik = PIDX[i][k], jk = PIDX[j][k];
            int d = PR(F[nbp[x * 4 + i] * 6 + jk]) - PR(F[x * 6 + jk])
                  - PR(F[nbp[x * 4 + j] * 6 + ik]) + PR(F[x * 6 + ik])
                  + PR(F[nbp[x * 4 + k] * 6 + ij]) - PR(F[x * 6 + ij]);
            if (d != 0) { nmono++; mabs += (d > 0 ? d : -d) / N; }
        }
    }
    /* integer flux through every coordinate 2-plane */
    long nzp = 0; int fmax = 0; double fmean[6];
    long *fl = calloc((size_t)L * L, sizeof(long));
    for (int a = 0; a < 6; a++) {
        int mu = PL[a][0], nu = PL[a][1], rho = -1, sig = -1;
        for (int t = 0; t < 4; t++) if (t != mu && t != nu) { if (rho < 0) rho = t; else sig = t; }
        memset(fl, 0, sizeof(long) * L * L);
        for (int x = 0; x < V; x++) fl[crd[x * 4 + rho] * L + crd[x * 4 + sig]] += PR(F[x * 6 + a]);
        double sm = 0;
        for (int q = 0; q < L * L; q++) {
            if (fl[q] % N != 0) { fprintf(stderr, "INTEGRITY plane flux not a multiple of N\n"); exit(3); }
            long ph = fl[q] / N;          /* exact: plane sum is a multiple of N */
            sm += (double)ph;
            if (ph != 0) nzp++;
            int ab = (int)(ph > 0 ? ph : -ph);
            if (ab > fmax) fmax = ab;
        }
        fmean[a] = sm / (L * L);
    }
    free(fl);
#undef PR
    /* Polyakov radius, averaged over directions */
    double rad = 0;
    for (int mu = 0; mu < 4; mu++) {
        double pr = 0, pi = 0;
        for (int x = 0; x < V; x++) {
            if (crd[x * 4 + mu] != 0) continue;
            int h = 0, y = x;
            for (int st = 0; st < L; st++) { h += U[y * 4 + mu]; y = nbp[y * 4 + mu]; }
            h = md(h);
            pr += cosT[h]; pi += sinT[h];
        }
        double n3 = (double)V / L;
        rad += sqrt(pr * pr + pi * pi) / n3 / 4.0;
    }
    printf("M sweep=%ld cos=%.10f logw=%.10f x2=%.10f mono=%.10f mlen=%.10f polrad=%.10f "
           "A1=%.10e B1=%.10e A2=%.10e B2=%.10e fnz=%.8f fmax=%d fm01=%.6f fm02=%.6f fm03=%.6f fm12=%.6f fm13=%.6f fm23=%.6f\n",
           sweepno, sumcos / (6.0 * V), sumlogw / (6.0 * V), sumx2 / (6.0 * V), (double)nmono / (4.0 * V),
           (double)mabs / (4.0 * V), rad, A[0], B[0], A[1], B[1], (double)nzp / (6.0 * L * L), fmax,
           fmean[0], fmean[1], fmean[2], fmean[3], fmean[4], fmean[5]);
    if (docorr) {
        printf("C sweep=%ld", sweepno);
        for (int n = 1; n <= L / 2; n++) {
            double lr = 0, tr = 0;
            for (int a = 0; a < 6; a++) {
                for (int rho = 0; rho < 4; rho++) {
                    int longi = (PL[a][0] == rho || PL[a][1] == rho);
                    for (int x = 0; x < V; x++) {
                        int y = x;
                        for (int st = 0; st < n; st++) y = nbp[y * 4 + rho];
                        int f1 = F[x * 6 + a], f2 = F[y * 6 + a];
                        if (longi) lr += cosT[f1] * cosT[f2] - sinT[f1] * sinT[f2];
                        else tr += cosT[f1] * cosT[f2] + sinT[f1] * sinT[f2];
                    }
                }
            }
            printf(" L%d=%.10e T%d=%.10e", n, lr / (12.0 * V), n, tr / (12.0 * V));
        }
        printf("\n");
    }
    fflush(stdout);
}

int main(int argc, char **argv) {
    if (argc < 9) { fprintf(stderr, "usage: zlgt2 N L seed cold|hot ntherm nmeas every corr_every W.. X..\n"); return 2; }
    N = atoi(argv[1]); L = atoi(argv[2]);
    if (N < 2 || N > 64 || L < 2 || L > 64) { fprintf(stderr, "bad N or L\n"); return 2; }
    uint64_t seed = strtoull(argv[3], NULL, 0);
    int hot = strcmp(argv[4], "hot") == 0;
    if (!hot && strcmp(argv[4], "cold") != 0 && strcmp(argv[4], "selftest") != 0) { fprintf(stderr, "start must be cold, hot or selftest\n"); return 2; }
    long ntherm = atol(argv[5]), nmeas = atol(argv[6]), every = atol(argv[7]), cevery = atol(argv[8]);
    if (argc != 9 + 2 * N) { fprintf(stderr, "need %d weights and %d scores\n", N, N); return 2; }
    for (int f = 0; f < N; f++) { Wt[f] = atof(argv[9 + f]); Xt[f] = atof(argv[9 + N + f]); }
    for (int f = 0; f < N; f++) {
        if (!(Wt[f] > 0)) { fprintf(stderr, "weights must be positive\n"); return 2; }
        if (fabs(Wt[f] - Wt[(N - f) % N]) > 1e-12 * Wt[f]) { fprintf(stderr, "weights must be symmetric\n"); return 2; }
        if (fabs(Xt[f] + Xt[(N - f) % N]) > 1e-12 * (1 + fabs(Xt[f]))) { fprintf(stderr, "score must be odd\n"); return 2; }
        logWt[f] = log(Wt[f]); cosT[f] = cos(2 * M_PI * f / N); sinT[f] = sin(2 * M_PI * f / N);
    }
    for (int a = 0; a < 6; a++) { PIDX[PL[a][0]][PL[a][1]] = a; PIDX[PL[a][1]][PL[a][0]] = a; }
    seedrng(seed);
    geometry();
    U = malloc((size_t)V * 4);
    F = malloc((size_t)V * 6);
    marg = malloc(sizeof(double) * 6 * 4 * L);
    R = malloc(sizeof(double) * N * N);
    build_table();
    int selftest = strcmp(argv[4], "selftest") == 0;
    for (int i = 0; i < V * 4; i++) U[i] = (hot || selftest) ? (uint8_t)(next64() % (uint64_t)N) : 0;
    if (selftest) {
        /* compare the rolled-table conditional with a brute-force recomputation of
           the six plaquettes through plaq(), on random links of a random state */
        double worst = 0; double p[64], q[64];
        for (int trial = 0; trial < 20000; trial++) {
            int x = (int)(next64() % (uint64_t)V), mu = (int)(next64() % 4);
            const double *row[6]; int k = 0; int xpmu = nbp[x * 4 + mu];
            for (int nu = 0; nu < 4; nu++) {
                if (nu == mu) continue;
                int xpnu = nbp[x * 4 + nu], xmnu = nbm[x * 4 + nu];
                int s1 = U[xpmu * 4 + nu] - U[xpnu * 4 + mu] - U[x * 4 + nu];
                int s2 = U[xmnu * 4 + mu] + U[nbp[xmnu * 4 + mu] * 4 + nu] - U[xmnu * 4 + nu];
                row[k++] = R + md(s1) * N; row[k++] = R + md(-s2) * N;
            }
            double tp = 0, tq = 0; uint8_t keep = U[x * 4 + mu];
            for (int u = 0; u < N; u++) {
                p[u] = row[0][u] * row[1][u] * row[2][u] * row[3][u] * row[4][u] * row[5][u]; tp += p[u];
                U[x * 4 + mu] = (uint8_t)u;
                double w = 1;
                for (int nu = 0; nu < 4; nu++) {
                    if (nu == mu) continue;
                    w *= Wt[plaq(x, mu, nu)] * Wt[plaq(nbm[x * 4 + nu], mu, nu)];
                }
                q[u] = w; tq += w;
            }
            U[x * 4 + mu] = keep;
            for (int u = 0; u < N; u++) { double d = fabs(p[u] / tp - q[u] / tq); if (d > worst) worst = d; }
        }
        printf("SELFTEST N=%d L=%d trials=20000 max_abs_prob_diff=%.3e %s\n", N, L, worst, worst < 1e-12 ? "PASS" : "FAIL");
        return worst < 1e-12 ? 0 : 1;
    }
    printf("RUN engine=zlgt2 N=%d L=%d seed=%s start=%s ntherm=%ld nmeas=%ld every=%ld corr_every=%ld\n",
           N, L, argv[3], argv[4], ntherm, nmeas, every, cevery);
    fflush(stdout);
    for (long t = 0; t < ntherm; t++) sweep();
    long sw = ntherm;
    for (long mm = 0; mm < nmeas; mm++) {
        for (long e = 0; e < every; e++) { sweep(); sw++; }
        measure(sw, cevery > 0 && (mm % cevery) == 0);
    }
    uint64_t h = 1469598103934665603ULL;
    for (int i = 0; i < V * 4; i++) { h ^= U[i]; h *= 1099511628211ULL; }
    printf("END sweeps=%ld state_fnv1a=%016llx\n", sw, (unsigned long long)h);
    return 0;
}
