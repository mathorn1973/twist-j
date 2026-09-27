# RUN - C-PHOTON-POLYMER-CONTEXT-GRAMMAR-N3

**Status:** NON-CANONICAL exact audit.
**Owner:** #1206.
**Scientific ceiling:** candidate-C for this frozen certificate protocol.

## Custody

- PREREG commit:
  \`dc6f6699bc657b012a992ecd92e38d990072026f\`
- verifier commit:
  \`ec303fe4fc85f4a7a7bfe8c609c2de9664a06129\`
- PREREG blob:
  \`bdcf733daea1fae19d0f04ae344415f5012b7ddc\`
- verifier blob:
  \`d39cefbfca65205038043997acf0b2afe2a21c05\`
- PREREG SHA-256:
  \`c7ad2a23aedf25b71f52651597ed29f27abd7148175906fddd969ad334a65dd2\`
- verifier SHA-256:
  \`90fb453261b888050ea0249044c9ebc05e87dab7f3587bdbf4189a65f58e3cc4\`

Both files were publicly read back from GitHub before execution.

## First scientific execution

The frozen wall-clock budget was 45 seconds. A Python subprocess supervisor
enforced that exact budget.

Environment:

\`\`\`text
architecture: aarch64
python: Python 3.12.3
head: ec303fe4fc85f4a7a7bfe8c609c2de9664a06129
completed: yes
elapsed_lt_45_5: True
exit_code: 0
stdout_bytes: 865
stderr_bytes: 0
\`\`\`

Exact scientific stdout:

\`\`\`text
GRAMMAR PASS states=17874 root_monomials=1240 transition_monomials=3157116 unique_transition_terms=3157116 max_uncles=5 max_survivors=15 max_children=5 candidate_graphs=6973
Y_ATTEMPT y=17/16 disposition=COORD_CAP iterations=5 max_q=322777/262144
Y_ATTEMPT y=33/32 disposition=COORD_CAP iterations=5 max_q=265491/262144
Y_ATTEMPT y=65/64 disposition=COORD_CAP iterations=6 max_q=515991/65536
Y_ATTEMPT y=129/128 disposition=COORD_CAP iterations=6 max_q=916587/131072
Y_ATTEMPT y=257/256 disposition=COORD_CAP iterations=6 max_q=54027/8192
Y_ATTEMPT y=513/512 disposition=COORD_CAP iterations=6 max_q=1679311/262144
Y_ATTEMPT y=1025/1024 disposition=COORD_CAP iterations=6 max_q=827597/131072
Y_ATTEMPT y=1 disposition=COORD_CAP iterations=6 max_q=1631345/262144
CONTEXT_GRAMMAR_CERTIFICATE NONE
AUDIT PASS; context_grammar_protocol=NO_CERTIFICATE; Xi=OPEN; P1=OPEN
\`\`\`

No parameter was changed after execution.
