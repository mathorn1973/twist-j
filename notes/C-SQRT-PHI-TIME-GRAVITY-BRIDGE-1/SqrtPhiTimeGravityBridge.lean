/-
  C-SQRT-PHI-TIME-GRAVITY-BRIDGE-1, selector-free bridge contract.
  NON-CANONICAL incubation file, no authority. The row stays O.
  Basis: Public Canon v101 (tag canon-v101). Lean 4 + Mathlib, no sorry.
  F_25 is modelled explicitly as pairs over Fin 5 (arithmetic mod 5),
  (a, b) meaning a + b tau with tau^2 = 2. Every finite fact is closed by
  `decide`; the all-n statements follow from period eight of the roots.
-/
import Mathlib

namespace SqrtPhiTimeGravity

/-! Frozen lemmas of SQRT-PHI-DIGIT-LIFT, restated. If the original module is
available, import it and delete these two copies; the statements match. -/

/-- binary digit sum, as frozen -/
def s2 (n : ℕ) : ℕ := (Nat.digits 2 n).sum

theorem branch_relation {R : Type*} [CommRing R] (r : R) (k : ℕ) :
    (-r) ^ k = (-1) ^ k * r ^ k :=
  neg_pow r k

theorem branch_sequence {R : Type*} [CommRing R] (r : R) (n : ℕ) :
    (-r) ^ s2 n = (-1) ^ (s2 n % 2) * r ^ s2 n := by
  rw [branch_relation]
  congr 1
  conv_lhs => rw [← Nat.mod_add_div (s2 n) 2]
  rw [pow_add, pow_mul, neg_one_sq, one_pow, mul_one]

/-! F_25 = F_5[tau]/(tau^2 - 2) -/

abbrev F5 := Fin 5
abbrev F25 := F5 × F5

def one : F25 := (1, 0)
def mul (x y : F25) : F25 := (x.1 * y.1 + 2 * x.2 * y.2, x.1 * y.2 + x.2 * y.1)
def neg (x : F25) : F25 := (4 * x.1, 4 * x.2)

def pw (x : F25) : ℕ → F25
  | 0 => one
  | k + 1 => mul x (pw x k)

theorem pw_succ (x : F25) (k : ℕ) : pw x (k + 1) = mul x (pw x k) := rfl

def tau : F25 := (0, 1)
def eta : F25 := pw tau 3
def phiF : F25 := (3, 0)

/-- norm F_25 -> F_5: N(a + b tau) = a^2 - 2 b^2 -/
def N (x : F25) : F5 := x.1 * x.1 - 2 * x.2 * x.2

/-- square class F_5^* -> C2: 0 on {1, 4}, 1 on {2, 3} -/
def q (t : F5) : ℕ := if t = 1 ∨ t = 4 then 0 else 1

/-- the model encodes the frozen data: eta = (0,2), eta^2 = phi, order 8,
    N(eta) = 2, and -eta is also a root of r^2 = phi -/
theorem frozen_field_data :
    eta = (0, 2) ∧ mul eta eta = phiF ∧ pw eta 8 = one ∧ pw eta 4 ≠ one ∧
      N eta = 2 ∧ mul (neg eta) (neg eta) = phiF := by
  decide

inductive Branch where
  | plus
  | minus
  deriving DecidableEq

def root : Branch → F25
  | .plus => eta
  | .minus => neg eta

/-- the frozen unique solution Y_n = r_eps ^ s_2(n) -/
def Y (e : Branch) (n : ℕ) : F25 := pw (root e) (s2 n)

/-- frozen readout R = Theta = N(Y) -/
def Theta (e : Branch) (n : ℕ) : F5 := N (Y e n)

/-- Thue-Morse bit of native U -/
def theta (n : ℕ) : ℕ := s2 n % 2

/-! Period eight of both roots -/

theorem pw_root_period (e : Branch) (k : ℕ) : pw (root e) (k + 8) = pw (root e) k := by
  induction k with
  | zero => cases e <;> decide
  | succ k ih =>
    show pw (root e) (k + 1 + 8) = pw (root e) (k + 1)
    have h : k + 1 + 8 = (k + 8) + 1 := by omega
    rw [h, pw_succ (root e) (k + 8), ih]
    exact (pw_succ (root e) k).symm

theorem pw_root_mul8 (e : Branch) (j m : ℕ) : pw (root e) (8 * m + j) = pw (root e) j := by
  induction m with
  | zero => simp
  | succ m ih =>
    show pw (root e) (8 * (m + 1) + j) = pw (root e) j
    have h : 8 * (m + 1) + j = (8 * m + j) + 8 := by omega
    rw [h, pw_root_period, ih]

theorem pw_root_mod8 (e : Branch) (k : ℕ) : pw (root e) k = pw (root e) (k % 8) := by
  conv_lhs => rw [← Nat.div_add_mod k 8]
  exact pw_root_mul8 e (k % 8) (k / 8)

/-! Clock leg: Y -> Theta -> theta -/

theorem readout_parity (e : Branch) (k : ℕ) : q (N (pw (root e) k)) = k % 2 := by
  have key : ∀ j : Fin 8, q (N (pw (root e) j.val)) = j.val % 2 := by
    cases e <;> decide
  have h : q (N (pw (root e) (k % 8))) = k % 8 % 2 :=
    key ⟨k % 8, Nat.mod_lt _ (by norm_num)⟩
  rw [pw_root_mod8, h]
  omega

/-- pre-update record at the checkpoint with counter n -/
def clockRead (e : Branch) (n : ℕ) : ℕ := q (Theta e n)

theorem clock_bridge (e : Branch) (n : ℕ) : clockRead e n = theta n :=
  readout_parity e (s2 n)

/-! Connection to the sigma law of native U, pre-update convention -/

def z6 (psi : Fin 6 → F5) : F5 := psi 0 + psi 1 + psi 2 + psi 3 + psi 4 + psi 5
def bitF5 (t : ℕ) : F5 := if t % 2 = 0 then 0 else 1

/-- sigma(omega) = z_6(psi) + 2 theta_n mod 5 at omega = (n, psi) -/
def sigmaU (omega : ℕ × (Fin 6 → F5)) : F5 := z6 omega.2 + 2 * bitF5 (theta omega.1)

theorem sigma_pre_update (e : Branch) (omega : ℕ × (Fin 6 → F5)) :
    z6 omega.2 + 2 * bitF5 (clockRead e omega.1) = sigmaU omega := by
  unfold sigmaU
  rw [clock_bridge]

/-! Gravity leg: the constant g of GRAVITY-BRIDGE-LAW -/

noncomputable def phiR : ℝ := (1 + Real.sqrt 5) / 2
noncomputable def g : ℝ := 2 ^ 5 * phiR ^ 2 * Real.sqrt (3 - phiR)
noncomputable def gravityRead (_e : Branch) (_n : ℕ) : ℝ := g

theorem gravity_leg_constant (e e' : Branch) (n n' : ℕ) :
    gravityRead e n = gravityRead e' n' := rfl

/-! The bridge on the declared domain N_0 x {+,-} -/

noncomputable def bridge (e : Branch) (n : ℕ) : ℕ × ℝ := (clockRead e n, gravityRead e n)

/-- total compatibility: for every n and both branches the bridge returns
    exactly (theta_n, g) -/
theorem bridge_total_compatible (e : Branch) (n : ℕ) : bridge e n = (theta n, g) := by
  show (clockRead e n, g) = (theta n, g)
  rw [clock_bridge]

/-- sign invariance of the complete readout, no selector -/
theorem bridge_sign_invariant (n : ℕ) : bridge .plus n = bridge .minus n := by
  rw [bridge_total_compatible, bridge_total_compatible]

end SqrtPhiTimeGravity
