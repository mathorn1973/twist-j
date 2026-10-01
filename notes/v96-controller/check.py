"""Reproduce development tests; writes generated fixtures outside the checkout."""
import argparse
import hashlib
import os
from pathlib import Path
import subprocess
import sys


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--tool-root',type=Path,help='optional extracted Debian package prefix')
    args=parser.parse_args()
    source=Path(__file__).resolve().parent
    root=source.parents[1]
    output=args.output.resolve()
    if output==root or root in output.parents:
        parser.error('generated files must be outside this checkout')
    output.mkdir(parents=True,exist_ok=True)
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
    def run(command):
        subprocess.run(list(map(str,command)),cwd=root,env=env,check=True)
    run([sys.executable,'-m','unittest','discover','-s',source,'-p','test_runtime.py'])
    run([sys.executable,source/'rtl_vectors.py',output/'vectors.txt'])
    compiler=['iverilog']
    simulator='vvp'
    if args.tool_root:
        prefix=args.tool_root.resolve()
        compiler=[prefix/'usr/bin/iverilog','-B',prefix/'usr/lib/x86_64-linux-gnu/ivl']
        simulator=prefix/'usr/bin/vvp'
    run(compiler+['-V'])
    for name in ('law','controller'):
        sources=[source/'law.v']
        if name=='controller': sources.append(source/'controller.v')
        run(compiler+['-g2012','-s',name+'_tb','-o',output/(name+'.vvp')]+sources+[source/(name+'_tb.v')])
        command=[simulator,output/(name+'.vvp')]
        if name=='law': command.append('+vectors='+str(output/'vectors.txt'))
        run(command)
    for path in sorted(source.glob('*')):
        if path.is_file():
            print('SOURCE',path.name,hashlib.sha256(path.read_bytes()).hexdigest())
    print('SOFTWARE_AND_SIMULATION_ONLY; PLACE_ROUTE_AND_HIL_NOT_RUN')


if __name__=='__main__': main()
