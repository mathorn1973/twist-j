#!/bin/bash
cd "$(dirname "$0")"
echo "job start $(date)" > run_6366_r8.log
python3 -u repair_witness.py 6 3 6 6 8 3000 >> run_6366_r8.log 2>&1
echo "job end $(date) exit $?" >> run_6366_r8.log
