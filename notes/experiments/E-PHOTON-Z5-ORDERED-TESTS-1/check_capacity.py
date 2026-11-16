"""PRE-PIN deterministic geometry only; no RNG, configurations or Gibbs draws."""
from itertools import combinations
from prepare_capacity import prepare

def check():
    outputs = prepare()
    assert b"6 * 64" in outputs["photon_z5_part2.inc"]
    assert b"std::adjacent_find(sorted_ids.begin(), end)" in outputs["photon_z5_part2.inc"]
    collision_cases = [[], [0], list(range(384)), [0, 0], [7, 2, 7], list(range(383)) + [0]]
    for ids in collision_cases:
        original = any(ids[i] == ids[j] for i in range(len(ids)) for j in range(i + 1, len(ids)))
        ordered = sorted(ids)
        replacement = any(a == b for a, b in zip(ordered, ordered[1:]))
        assert original == replacement
    pairs = list(combinations(range(4), 2))
    checked = 0
    for L in range(2, 65):
        volume = L**4
        assert volume < 2**31 and 6 * volume < 2**31
        assert 4 * volume < 2**32 and 4 * L**3 < 2**32
        for mu in range(4):
            # Translations biject both face labels and all transverse anchors.
            # Origin and far-corner anchors explicitly exercise periodic wrap.
            for anchor in (0, L - 1):
                base = [anchor] * 4
                base[mu] = 0
                faces = []
                for step in range(L):
                    site = base.copy()
                    site[mu] = step
                    for nu in range(4):
                        if nu == mu:
                            continue
                        pair = pairs.index(tuple(sorted((mu, nu))))
                        for shift in (0, -1):
                            pos = site.copy()
                            pos[nu] = (pos[nu] + shift) % L
                            encoded = 0
                            for x in pos:
                                encoded = encoded * L + x
                            faces.append(6 * encoded + pair)
                assert len(faces) == 6 * L <= 384
                assert len(set(faces)) == len(faces)
                assert max(faces) < 6 * volume
                checked += 1
    print("PREPIN_GEOMETRY_ONLY cases=" + str(checked) + " L=2..64 PASS")
    print("PREPIN_COLLISION_NEGATIVE_AND_POSITIVE_CONTROLS cases=6 PASS")
    print("L64_base_arrays_bytes=" + str(58 * 64**4))
    print("L64_constructor_duplicate_comparisons=" + str(4 * 64**3 * (384 * 383 // 2)))

if __name__ == "__main__":
    check()
