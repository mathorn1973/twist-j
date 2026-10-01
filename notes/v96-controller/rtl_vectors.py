"""Write finite SOFTWARE fixtures to a caller-chosen untracked path."""
import sys
from pathlib import Path
from test_runtime import cases, reference


def pack(state):
    return sum((v & 65535) << (16*i) for i,v in enumerate(state))


def write(path):
    ref=reference();count=0
    with Path(path).open('w',encoding='ascii',newline='\n') as stream:
        for state in cases():
            for inverse in (False,True):
                for cut in (None,0,1):
                    current=state
                    for kind,expected in ref.layers(state,3,cut=cut,inverse=inverse):
                        fields=(pack(current[:-1]),current[-1],'GABF'.index(kind[0]),
                                int(inverse),0 if cut is None else 1<<cut,1,
                                pack(expected[:-1]),expected[-1])
                        stream.write(' '.join(format(v,'x') for v in fields)+'\n')
                        current=expected;count+=1
        for value in (32767,-32768,7):
            state=[0]*95;state[0]=value
            stream.write(f'{pack(state):x} 0 0 0 0 0 {pack(state):x} 0\n');count+=1
        stream.write('0 5 0 0 0 0 0 5\n');count+=1
    print(f'SOFTWARE vectors={count}; no measured inputs')


if __name__=='__main__': write(sys.argv[1])
