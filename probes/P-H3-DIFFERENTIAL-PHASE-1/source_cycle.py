# SPDX-License-Identifier: Apache-2.0
"""Check an exact complete-state return of the undriven, isolated source."""

from anchored import DELTA, J, ZERO, account, collisions, contacts
from emitter import CENTER
from native import h3

SIZE = 24
BOUND = 340
CENTER_XY = SIZE//2


def run():
    z = CENTER_XY
    start = {(z,z,0):DELTA, (z,z,1):h3.scale(-1,DELTA),
             (z,z,2):h3.mul(DELTA,h3.add(CENTER,J)),
             (z,z,3):h3.mul(DELTA,h3.sub(CENTER,J))}
    stock = account(start)
    current = start
    radius = 0
    support = set()
    events = []
    period = None
    for tick in range(1,BOUND+1):
        bit = (tick-1)%2
        pre = contacts(current,bit,nx=SIZE,ny=SIZE)
        post,tags = collisions(pre)
        back,_ = collisions(post)
        assert back==pre and contacts(back,bit,True,nx=SIZE,ny=SIZE)==current
        assert account(pre)==account(post)==stock
        for state in (pre,post):
            for x,y,i in state:
                radius = max(radius,abs(x-z),abs(y-z))
                support.add((x-z,y-z,i))
        events.extend((tick,x-z,y-z,t) for (x,y),t in sorted(tags.items()))
        current = post
        if tick%2==0 and current==start:
            period = tick
            break
    return {"tick_limit":BOUND,"ticks_checked":tick,"first_full_return_with_matching_bit":period,
            "max_coordinate_radius_through_both_substeps":radius,
            "lifts_to_unbounded_grid":period is not None and radius < SIZE//2-1,
            "source_B_tags":events,"nonzero_site_rail_union":sorted(support)}
