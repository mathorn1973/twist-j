/* zlgt.c : independent Z_N lattice gauge heat-bath with arbitrary plaquette
 * weight table, 4D periodic L^4. Engineering orientation engine for
 * C-PHOTON-PHASE-ORIENTATION-N (NON-CANONICAL). Floating point categorical
 * draws; this engine makes no exact-arithmetic claim.
 *
 * usage: zlgt N L seed start(cold|hot) ntherm nmeas every corr_every W0..W{N-1} X0..X{N-1}
 * Output: one line per measurement, see print statements.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static int N, L, V;
static uint8_t *U;           /* U[x*4+mu] */
static int *nbp, *nbm;       /* nbp[x*4+mu] = x+e_mu, nbm = x-e_mu */
static double Wt[256], Xt[256], logWt[256];
static double cosT[256], sinT[256];

static uint64_t s[4];
static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static uint64_t next64(void) {
    const uint64_t result = rotl(s[1] * 5, 7) * 9;
    const uint64_t t = s[1] << 17;
    s[2] ^= s[0]; s[3] ^= s[1]; s[1] ^= s[2]; s[0] ^= s[3]; s[2] ^= t; s[3] = rotl(s[3], 45);
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
        s[i] = y ^ (y >> 31);
    }
}

static inline int md(int a) { a %= N; return a < 0 ? a + N : a; }

static void geometry(void) {
    V = L * L * L * L;
    nbp = malloc(sizeof(int) * V * 4);
    nbm = malloc(sizeof(int) * V * 4);
    for (int x = 0; x < V; x++) {
        int c[4], t = x;
        for (int mu = 3; mu >= 0; mu--) { c[mu] = t % L; t /= L; }
        for (int mu = 0; mu < 4; mu++) {
            int cp[4], cm[4];
            memcpy(cp, c, sizeof c); memcpy(cm, c, sizeof c);
            cp[mu] = (c[mu] + 1) % L; cm[mu] = (c[mu] + L - 1) % L;
            nbp[x * 4 + mu] = ((cp[0] * L + cp[1]) * L + cp[2]) * L + cp[3];
            nbm[x * 4 + mu] = ((cm[0] * L + cm[1]) * L + cm[2]) * L + cm[3];
        }
    }
}

static inline int plaq(int x, int mu, int nu) {
    return md(U[x * 4 + mu] + U[nbp[x * 4 + mu] * 4 + nu] - U[nbp[x * 4 + nu] * 4 + mu] - U[x * 4 + nu]);
}

static void sweep(void) {
    double p[256];
    for (int x = 0; x < V; x++) {
        for (int mu = 0; mu < 4; mu++) {
            int s1[3], s2[3], k = 0;
            for (int nu = 0; nu < 4; nu++) {
                if (nu == mu) continue;
                int xpmu = nbp[x * 4 + mu], xpnu = nbp[x * 4 + nu], xmnu = nbm[x * 4 + nu];
                s1[k] = U[xpmu * 4 + nu] - U[xpnu * 4 + mu] - U[x * 4 + nu];
                s2[k] = U[xmnu * 4 + mu] + U[nbp[xmnu * 4 + mu] * 4 + nu] - U[xmnu * 4 + nu];
                k++;
            }
            double tot = 0;
            for (int u = 0; u < N; u++) {
                double w = 1.0;
                for (int j = 0; j < 3; j++) w *= Wt[md(u + s1[j])] * Wt[md(u - s2[j])];
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

static void measure(long sweepno, int docorr) {
    /* local and Fourier observables */
    double sumcos = 0, sumlogw = 0, sumx2 = 0;
    int ncoord[4];
    double re[4][2][6], im[4][2][6]; /* axis mu, m=1,2, plane a */
    memset(re, 0, sizeof re); memset(im, 0, sizeof im);
    double *X = malloc(sizeof(double) * V * 6);
    int *F = malloc(sizeof(int) * V * 6);
    for (int x = 0; x < V; x++) {
        int t = x;
        for (int mu = 3; mu >= 0; mu--) { ncoord[mu] = t % L; t /= L; }
        for (int a = 0; a < 6; a++) {
            int f = plaq(x, PL[a][0], PL[a][1]);
            F[x * 6 + a] = f;
            double xv = Xt[f];
            X[x * 6 + a] = xv;
            sumcos += cosT[f]; sumlogw += logWt[f]; sumx2 += xv * xv;
            for (int mu = 0; mu < 4; mu++) {
                for (int m = 1; m <= 2; m++) {
                    double ph = 2 * M_PI * m * ncoord[mu] / L;
                    re[mu][m - 1][a] += xv * cos(ph);
                    im[mu][m - 1][a] -= xv * sin(ph);
                }
            }
        }
    }
    double A[2] = {0, 0}, B[2] = {0, 0};
    for (int mu = 0; mu < 4; mu++)
        for (int m = 0; m < 2; m++)
            for (int a = 0; a < 6; a++) {
                double pw = (re[mu][m][a] * re[mu][m][a] + im[mu][m][a] * im[mu][m][a]) / V;
                int contains = (PL[a][0] == mu || PL[a][1] == mu);
                if (contains) A[m] += pw / 12.0; else B[m] += pw / 12.0;
            }
    /* monopoles: cube (x; i<j<k) with dF over principal representative */
    long nmono = 0, ncube = 0;
    for (int x = 0; x < V; x++) {
        for (int i = 0; i < 4; i++) for (int j = i + 1; j < 4; j++) for (int k = j + 1; k < 4; k++) {
            /* oriented boundary of cube [i,j,k]: +F_jk(x+i) - F_jk(x) - F_ik(x+j) + F_ik(x) + F_ij(x+k) - F_ij(x) */
            int idx_ij = -1, idx_ik = -1, idx_jk = -1;
            for (int a = 0; a < 6; a++) {
                if (PL[a][0] == i && PL[a][1] == j) idx_ij = a;
                if (PL[a][0] == i && PL[a][1] == k) idx_ik = a;
                if (PL[a][0] == j && PL[a][1] == k) idx_jk = a;
            }
            int half = N / 2;
#define PR(v) ((v) > half ? (v) - N : (v))
            int d = PR(F[nbp[x * 4 + i] * 6 + idx_jk]) - PR(F[x * 6 + idx_jk])
                  - PR(F[nbp[x * 4 + j] * 6 + idx_ik]) + PR(F[x * 6 + idx_ik])
                  + PR(F[nbp[x * 4 + k] * 6 + idx_ij]) - PR(F[x * 6 + idx_ij]);
#undef PR
            ncube++;
            if (d != 0) nmono++;
        }
    }
    /* Polyakov radius */
    double rad = 0;
    for (int mu = 0; mu < 4; mu++) {
        double pr = 0, pi = 0;
        for (int x = 0; x < V; x++) {
            int t = x, c[4];
            for (int q = 3; q >= 0; q--) { c[q] = t % L; t /= L; }
            if (c[mu] != 0) continue;
            int h = 0, y = x;
            for (int st = 0; st < L; st++) { h += U[y * 4 + mu]; y = nbp[y * 4 + mu]; }
            h = md(h);
            pr += cosT[h]; pi += sinT[h];
        }
        double n3 = (double)V / L;
        rad += sqrt(pr * pr + pi * pi) / n3 / 4.0;
    }
    printf("M sweep=%ld cos=%.10f logw=%.10f x2=%.10f mono=%.10f polrad=%.10f A1=%.10e B1=%.10e A2=%.10e B2=%.10e\n",
           sweepno, sumcos / (6.0 * V), sumlogw / (6.0 * V), sumx2 / (6.0 * V), (double)nmono / ncube, rad, A[0], B[0], A[1], B[1]);
    if (docorr) {
        /* frozen #757 orientation-sum ingredients: longitudinal E[W W'], transverse E[conj(W) W'] */
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
    free(X); free(F);
}

int main(int argc, char **argv) {
    if (argc < 9) { fprintf(stderr, "usage\n"); return 2; }
    N = atoi(argv[1]); L = atoi(argv[2]);
    uint64_t seed = strtoull(argv[3], NULL, 0);
    int hot = strcmp(argv[4], "hot") == 0;
    long ntherm = atol(argv[5]), nmeas = atol(argv[6]), every = atol(argv[7]), cevery = atol(argv[8]);
    if (argc != 9 + 2 * N) { fprintf(stderr, "need %d weights and %d scores\n", N, N); return 2; }
    for (int f = 0; f < N; f++) { Wt[f] = atof(argv[9 + f]); Xt[f] = atof(argv[9 + N + f]); logWt[f] = log(Wt[f]); }
    for (int f = 0; f < N; f++) { cosT[f] = cos(2 * M_PI * f / N); sinT[f] = sin(2 * M_PI * f / N); }
    seedrng(seed);
    geometry();
    U = malloc(V * 4);
    for (int i = 0; i < V * 4; i++) U[i] = hot ? (uint8_t)(next64() % (uint64_t)N) : 0;
    printf("RUN N=%d L=%d seed=%s start=%s ntherm=%ld nmeas=%ld every=%ld corr_every=%ld\n", N, L, argv[3], argv[4], ntherm, nmeas, every, cevery);
    for (long t = 0; t < ntherm; t++) sweep();
    long sw = ntherm;
    for (long mm = 0; mm < nmeas; mm++) {
        for (long e = 0; e < every; e++) { sweep(); sw++; }
        measure(sw, cevery > 0 && (mm % cevery) == 0);
    }
    return 0;
}
