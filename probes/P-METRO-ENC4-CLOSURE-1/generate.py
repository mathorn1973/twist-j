"""Generate a full finite ENC4 decision certificate; no checker import."""
import math
import sys


from auxiliary import auxiliary
from common import (
    aligned, boundary, digest, direction, dump, encoded, identity, limit_tables,
    mul, nonzero_point, norm, power, read, sub, system, transition,
)


def graph(axis):
    n = len(axis[0])
    edges = [tuple(sorted({f[s] for f in axis})) for s in range(n)]
    reach = []
    for source in range(n):
        visited = {source}
        todo = [source]
        for vertex in todo:
            for target in edges[vertex]:
                if target not in visited:
                    visited.add(target)
                    todo.append(target)
        reach.append(visited)
    classes = []
    todo = set(range(n))
    while todo:
        root = min(todo)
        component = {v for v in reach[root] if root in reach[v]}
        todo.difference_update(component)
        if component == reach[root]:
            classes.append(component)
    period = 1
    for component in classes:
        root = min(component)
        depth = {root: 0}
        queue = [root]
        for v in queue:
            for target in edges[v]:
                if target not in depth:
                    depth[target] = depth[v] + 1
                    queue.append(target)
        local = math.gcd(*(abs(depth[v] + 1 - depth[t])
                           for v in component for t in edges[v]))
        period = math.lcm(period, local)
    return period, set().union(*classes)


def rref(rows):
    data = [list(row) for row in rows]
    pivots = []
    for col in range(len(data[0])):
        index = len(pivots)
        found = next((j for j in range(index, len(data)) if data[j][col]), None)
        if found is None:
            continue
        data[index], data[found] = data[found], data[index]
        row = data[index]
        pivot = row[col]
        row[:] = [x / pivot for x in row]
        for j, other in enumerate(data):
            if j != index and other[col]:
                scale = other[col]
                other[:] = [x - scale * y for x, y in zip(other, row)]
        pivots.append(col)
    return data, pivots


def projection(p, h):
    n = len(p)
    diff = sub(identity(n), power(p, h))
    reduced, pivots = rref(diff)
    free = [j for j in range(n) if j not in pivots]
    eye = identity(n)
    kernel = []
    for j in free:
        col = list(eye[j])
        for i, pivot in enumerate(pivots):
            col[pivot] = -reduced[i][j]
        kernel.append(tuple(col))
    image = [tuple(row[j] for row in diff) for j in pivots]
    basis = tuple(zip(*(kernel + image)))
    inverse, _ = rref(tuple(left + right for left, right in zip(basis, eye)))
    projected = tuple(tuple(row[j] if j < len(kernel) else 0 for j in range(n))
                      for row in basis)
    return mul(projected, tuple(tuple(row[n:]) for row in inverse))


def killing(axis, closed, h, residue):
    image = set(range(len(axis[0])))
    word = []
    while not image <= closed:
        source = min(image - closed)
        todo = [(source, ())]
        seen = {source}
        for state, path in todo:
            if state in closed:
                for digit in path:
                    image = {axis[digit][v] for v in image}
                word.extend(path)
                break
            for digit, mapping in enumerate(axis):
                target = mapping[state]
                if target not in seen:
                    seen.add(target)
                    todo.append((target, path + (digit,)))
    word.extend([0] * ((residue - len(word)) % h))
    return word


def certificate(obj):
    s = system(obj)
    matrices = [transition(axis) for axis in s.digits]
    graphs = [graph(axis) for axis in s.digits]
    axes = []
    projections = []
    for p, (h, _) in zip(matrices, graphs):
        e = projection(p, h)
        k = h
        theta = norm(sub(power(p, k), e))
        while theta >= 1:
            k *= 2
            theta = norm(sub(power(p, k), e))
        projections.append(e)
        axes.append({"h": h, "E": [encoded(row) for row in e], "K": k, "theta": str(theta)})

    limits = limit_tables(matrices, projections, [axis["h"] for axis in axes])
    positive = boundary(s)
    point = nonzero_point(s, positive)
    rows = {}
    for row, witness in aligned(s, limits, positive):
        rows.setdefault(row, witness)
    first, *rest = rows
    raw = {"status": "RAW", "limit": encoded(first)} if not rest else {
        "status": "REJECT", "reason": "raw-split", "aligned": [rows[first], rows[rest[0]]],
    }
    if point is None:
        lit = {"status": "ZERO"}
    elif any(not any(row) for row in rows):
        zero = next(w for row, w in rows.items() if not any(row))
        words = []
        residues = []
        for axis, (h, closed), word, k in zip(s.digits, graphs, zero["words"], zero["residues"]):
            b = killing(axis, closed, h, k if s.msd else 0)
            words.append(word + b if s.msd else b + word)
            residues.append(0 if s.msd else k)
        lit = {"status": "REJECT", "reason": "tag-split", "point": point,
               "zero": {"start": zero["start"], "words": words, "residues": residues}}
    else:
        other = next((row for row in rest if direction(row) != direction(first)), None)
        if other is None:
            lit = {"status": "PROB", "limit": encoded(direction(first)),
                   "min_mass": str(min(sum(row) for row in rows))}
        else:
            lit = {"status": "REJECT", "reason": "direction-split",
                   "aligned": [rows[first], rows[other]]}
    return {"schema": "metro-enc4-v1", "system_sha256": digest(obj),
            "axes": axes, "raw": raw, "lit": lit, "auxiliary": auxiliary(s)}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: generate.py SYSTEM.json")
    try:
        print(dump(certificate(read(sys.argv[1]))))
    except (ValueError, OSError) as error:
        sys.exit(str(error))
