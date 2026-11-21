# SPDX-License-Identifier: Apache-2.0
"""Local algebra of the measured 159-to-181 interval on input 43."""
import kernel as k
import verify


def main():
    field = verify.launches()[43]
    bit = 1
    matter_ticks = {161, 163, 165, 167, 169, 173, 175, 177, 179, 181}
    clock_ticks = {162, 164, 166, 168, 170, 172, 174, 176, 178, 180}
    for tick in range(1, 182):
        pre = field
        contact, field = k.native_step(pre, bit)
        bit ^= 1
        if tick == 159:
            first_c, first_b = contact[28], field[28]
        if tick < 159:
            continue
        if tick in matter_ticks:
            pair = (31, 28)
            lane = k.R0
            midpoint = k.from_j(0, 0, 0, 1)
        elif tick in clock_ticks:
            pair = (28, 29)
            lane = k.CLK
            midpoint = k.from_j(0, 1, 0, 1)
        else:
            pair = None
        if pair is not None:
            a, b = [pre[i][lane] for i in pair]
            a1, b1 = [contact[i][lane] for i in pair]
            verify.check(k.even(k.subtract(a, b)), ("admission", tick))
            gap = k.half(k.subtract(a, b))
            rotated = k.multiply(k.RHO, gap)
            verify.check(k.half(k.add(a, b)) == midpoint and
                         (a1, b1) == (k.add(midpoint, rotated), k.subtract(midpoint, rotated)),
                         ("bond", tick))
        if tick in (159, 160, 167, 169, 170, 171, 179, 180, 181):
            verify.emit("local", dict(tick=tick, pre_word=k.reported(pre[31][0]),
                                      word_after_c=k.reported(contact[31][0]),
                                      worker_clk_after_c=k.reported(contact[28][2]),
                                      worker_r0_after_b=k.reported(field[28][0]),
                                      worker_b=k.scatter(contact[28])[1],
                                      memory_b=k.scatter(contact[31])[1]))
        if tick in (160, 171):
            verify.check(field[28] == first_c and k.scatter(contact[28])[1] == 1, ("B1 return", tick))
        if tick in (170, 181):
            verify.check(contact[28] == first_c and field[28] == first_b, ("B2 repeat", tick))


if __name__ == "__main__":
    main()
