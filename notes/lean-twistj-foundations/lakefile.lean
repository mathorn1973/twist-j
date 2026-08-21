import Lake
open Lake DSL

package TwistJFoundations where
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @
    "c5ea00351c28e24afc9f0f84379aa41082b1188f"

@[default_target]
lean_lib TwistJ where
  globs := #[`TwistJ.+]
