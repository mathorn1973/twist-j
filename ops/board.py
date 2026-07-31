#!/usr/bin/env python3
"""Board status. Reads ops/TASKS.tsv and every ops/log/*.log and prints who
should do what next. Standard library only. No writes, ever.

  python3 ops/board.py            full board
  python3 ops/board.py S3         what seat S3 should do next
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TASKS = os.path.join(ROOT, "TASKS.tsv")
LOGDIR = os.path.join(ROOT, "log")
EVENTS = ("CLAIM", "DONE", "BLOCKED", "STOP", "NOTE")
TERMINAL = {"DONE", "BLOCKED", "STOP"}


def read_tasks():
    out = []
    with open(TASKS, encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        if head != ["task_id", "seat", "depends_on", "object_key", "title"]:
            sys.exit("TASKS.tsv header is wrong: %s" % head)
        for n, line in enumerate(fh, start=2):
            line = line.rstrip("\n")
            if not line:
                continue
            f = line.split("\t")
            if len(f) != 5:
                sys.exit("TASKS.tsv line %d has %d fields, want 5" % (n, len(f)))
            deps = [] if f[2].strip() == "-" else f[2].split()
            out.append({"id": f[0], "seat": f[1], "deps": deps,
                        "object": f[3], "title": f[4]})
    ids = [t["id"] for t in out]
    if len(set(ids)) != len(ids):
        sys.exit("duplicate task_id in TASKS.tsv")
    for t in out:
        for d in t["deps"]:
            if d not in ids:
                sys.exit("task %s depends on unknown %s" % (t["id"], d))
    return out


def read_logs():
    """Every event, in file order per seat. Returns list of dicts."""
    evs = []
    for name in sorted(os.listdir(LOGDIR)):
        if not name.endswith(".log"):
            continue
        seat = name[:-4]
        path = os.path.join(LOGDIR, name)
        with open(path, encoding="utf-8") as fh:
            for n, line in enumerate(fh, start=1):
                line = line.rstrip("\n")
                if not line:
                    continue
                f = line.split("\t")
                if len(f) != 5:
                    sys.exit("%s line %d has %d fields, want 5" % (name, n, len(f)))
                if f[1] != seat:
                    sys.exit("%s line %d: seat field %s does not match the file"
                             % (name, n, f[1]))
                if f[3] not in EVENTS:
                    sys.exit("%s line %d: unknown event %s" % (name, n, f[3]))
                evs.append({"ts": f[0], "seat": f[1], "task": f[2],
                            "event": f[3], "detail": f[4], "src": name, "ln": n})
    return evs


def state_of(task_id, evs):
    """Last non-NOTE event for a task wins."""
    last = None
    for e in evs:
        if e["task"] == task_id and e["event"] != "NOTE":
            last = e
    return last


def main():
    tasks = read_tasks()
    evs = read_logs()
    states = {t["id"]: state_of(t["id"], evs) for t in tasks}

    def status(t):
        s = states[t["id"]]
        if s is not None:
            return s["event"]
        undone = [d for d in t["deps"] if not (states[d] and states[d]["event"] == "DONE")]
        return "READY" if not undone else "WAITING"

    want = sys.argv[1] if len(sys.argv) > 1 else None
    if want:
        rows = [t for t in tasks if t["seat"] == want]
        if not rows:
            print("no tasks for seat %s" % want)
            return
        nxt = [t for t in rows if status(t) == "READY"]
        print("SEAT %s" % want)
        if nxt:
            t = nxt[0]
            print("  NEXT: %s  %s" % (t["id"], t["title"]))
            print("  object: %s" % t["object"])
        else:
            openish = [t for t in rows if status(t) not in TERMINAL]
            if not openish:
                print("  nothing open. All your tasks are DONE, BLOCKED or STOP.")
            else:
                t = openish[0]
                print("  NOTHING READY. Next is %s (%s), waiting on: %s"
                      % (t["id"], status(t),
                         " ".join(d for d in t["deps"]
                                  if not (states[d] and states[d]["event"] == "DONE"))
                         or "itself"))
        print()

    print("%-7s %-4s %-9s %s" % ("TASK", "SEAT", "STATUS", "TITLE"))
    print("-" * 78)
    for t in tasks:
        st = status(t)
        mark = {"DONE": "  ", "READY": "->", "CLAIM": " *",
                "BLOCKED": "!!", "STOP": "!!"}.get(st, "  ")
        print("%s %-5s %-4s %-9s %.44s" % (mark, t["id"], t["seat"], st, t["title"]))
    print("-" * 78)
    counts = {}
    for t in tasks:
        counts[status(t)] = counts.get(status(t), 0) + 1
    print("  " + "  ".join("%s=%d" % (k, counts[k]) for k in sorted(counts)))
    stops = [t for t in tasks if status(t) in ("BLOCKED", "STOP")]
    if stops:
        print()
        print("ATTENTION:")
        for t in stops:
            s = states[t["id"]]
            print("  %s %s: %s" % (t["id"], s["event"], s["detail"]))


if __name__ == "__main__":
    main()
