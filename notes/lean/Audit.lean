import TwistJ

/-!
Axiom footprint of every declaration in the library. Expected output: only
`propext`, `Quot.sound` and, for the cyclotomic witness, `Classical.choice`.
Any `sorryAx` or project axiom is a failure.
-/

#print axioms TwistJ.Kernel.pow_five
#print axioms TwistJ.Kernel.J_mul_phi
#print axioms TwistJ.Kernel.J_sub_one_cube
#print axioms TwistJ.Kernel.phi_sq
#print axioms TwistJ.Kernel.phi_mul_psi
#print axioms TwistJ.Kernel.J_mul_inv
#print axioms TwistJ.Kernel.J_pow_five_mul_phi_pow_five
#print axioms TwistJ.Kernel.norm_J
#print axioms TwistJ.Kernel.trace_J
#print axioms TwistJ.Kernel.step_eq_mul_J
#print axioms TwistJ.Kernel.J_mul_Jbar
#print axioms TwistJ.Kernel.two_sub_phi_mul_phi_sq
#print axioms TwistJ.Kernel.one_sub_J
#print axioms TwistJ.Kernel.one_sub_J_pow_five
#print axioms TwistJ.Kernel.one_sub_J_pow_ten
#print axioms TwistJ.Kernel.J_charpoly
#print axioms TwistJ.Kernel.phi5_of_isPrimitiveRoot
#print axioms TwistJ.Kernel.phi5_cyclotomicField
