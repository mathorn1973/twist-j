#!/usr/bin/env python3
"""Exact audit for P-QDD-PASSIVE-READING-FAMILY-1.

No instrument, occurrence calendar, physical apparatus, pointer or reset.
Standalone exact arithmetic; imports no previous checker or repository file.
Its deterministic scientific output is LF on every supported platform.
"""
from fractions import Fraction as F
from itertools import product
import json
import sys

if not __debug__:
    raise RuntimeError('Optimized Python is not an accepted verifier environment')

sys.stdout.reconfigure(newline='\n')


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a,b):
    return [[sum((x*y for x,y in zip(row,col)),F(0))
             for col in zip(*b)] for row in a]


def madd(a,b):
    return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]


def mscale(a,q):
    return [[q*x for x in row] for row in a]


def outer(u,v,scale=1):
    return [[F(scale)*x*y for y in v] for x in u]


ID=[[F(i==j) for j in range(4)] for i in range(4)]
ZERO=[[F(0)]*4 for _ in range(4)]
G=[[F(i==j)-F(1,5) for j in range(4)] for i in range(4)]
E=(1,1,1,1)
CHI=(1,-1,-1,1)
U=(1,0,0,-1)
V=(0,1,-1,0)
P0=outer(E,E,F(1,4))
P1=outer(CHI,CHI,F(1,4))
P2=madd(outer(U,U,F(1,2)),outer(V,V,F(1,2)))
ATOMS=(P0,P1,P2)
PARTITIONS=(
    ((0,1,2),),
    ((0,),(1,2)),
    ((0,2),(1,)),
    ((0,1),(2,)),
    ((0,),(1,),(2,)),
)
PARTITION_IDS=('PI-ALL','PI-TRACE','PI-LEG','PI-PAIR','PI-ATOMS')
FAMILY=dict(zip(PARTITION_IDS,PARTITIONS))


def pblock(block):
    p=ZERO
    for a in block:
        p=madd(p,ATOMS[a])
    return p


def norm(v):
    return sum(x*x for x in v)-sum(v)**2/F(5)


def atom_masses(v):
    s=sum(v)
    ell=sum(x*y for x,y in zip(CHI,v))
    q=sum(x*x for x in v)
    return F(s*s,20),F(ell*ell,4),F(4*q-s*s-ell*ell,4)


def passive_vector_read(values,partition_id):
    """Mathematical Q^4 extension; adopted decoder enters through read_head."""
    v=tuple(F(x) for x in values)
    if len(v)!=4 or partition_id not in FAMILY:
        raise ValueError('Expected Q^4 and a declared partition')
    blocks=FAMILY[partition_id]
    if not any(v):
        return {'partition_id':partition_id,'support_state':'ZERO_SUPPORT',
                'total_weight':F(0),'block_weights':(F(0),)*len(blocks),
                'normalized_weight_state':'ZERO_DENOMINATOR'}
    masses=atom_masses(v)
    m=norm(v)
    raw=tuple(sum(masses[a] for a in b) for b in blocks)
    return {'partition_id':partition_id,'support_state':'SUPPORTED',
            'total_weight':m,'block_weights':raw,
            'normalized_weight_state':('NORMALIZED',tuple(w/m for w in raw))}


def read_head(head,partition_id):
    """R_pi on K_QDD via its existing beta_QDD head factorization only.

    A native head x determines kappa_x; q,r are forbidden as weight inputs.
    No future checkpoint, additional counter or environment is inspected.
    """
    head=tuple(head)
    if len(head)!=6 or any(type(x) is not int or not 0<=x<5 for x in head):
        raise ValueError('Native head must be in F_5^6')
    balanced=(0,1,2,-2,-1)
    return passive_vector_read(tuple(balanced[x] for x in head[:4]),partition_id)


def refines(sigma,pi):
    return all(any(set(fine)<=set(coarse) for coarse in FAMILY[pi])
               for fine in FAMILY[sigma])


RECORD_FIELDS={'partition_id','support_state','total_weight','block_weights',
               'normalized_weight_state'}


def is_rational(x):
    return type(x) is int or isinstance(x,F)


def coherent_record(record,sigma):
    """Recognize the declared sigma-specific domain of record coarsening."""
    if type(sigma) is not str or sigma not in FAMILY:
        return False
    if type(record) is not dict or set(record)!=RECORD_FIELDS:
        return False
    if record['partition_id']!=sigma:
        return False
    m,w=record['total_weight'],record['block_weights']
    if not is_rational(m) or type(w) is not tuple or len(w)!=len(FAMILY[sigma]):
        return False
    if any(not is_rational(x) or x<0 for x in w):
        return False
    tag=record['normalized_weight_state']
    if record['support_state']=='ZERO_SUPPORT':
        return m==0 and all(x==0 for x in w) and tag=='ZERO_DENOMINATOR'
    if record['support_state']!='SUPPORTED' or m<=0 or sum(w)!=m:
        return False
    if type(tag) is not tuple or len(tag)!=2 or tag[0]!='NORMALIZED':
        return False
    q=tag[1]
    return (type(q) is tuple and len(q)==len(w)
            and all(is_rational(x) for x in q)
            and all(x==F(y)/F(m) for x,y in zip(q,w)))


def generated_partitions(items):
    """Independent finite set-partition generation, without the five fixtures."""
    if not items:
        return {()}
    head,tail=items[0],items[1:]
    result=set()
    for blocks in generated_partitions(tail):
        result.add(tuple(sorted(((head,),)+blocks)))
        for i in range(len(blocks)):
            changed=list(blocks)
            changed[i]=tuple(sorted((head,)+changed[i]))
            result.add(tuple(sorted(changed)))
    return result


def coarsen(record,pi):
    """Map only the five-field snapshot record; does not touch source/history."""
    sigma=record.get('partition_id') if type(record) is dict else None
    if not coherent_record(record,sigma):
        raise ValueError('Expected a coherent record with its literal source ID')
    if type(pi) is not str or pi not in FAMILY:
        raise ValueError('Unknown target partition')
    if not refines(sigma,pi):
        raise ValueError('Not a refinement pair')
    groups=tuple(tuple(i for i,fine in enumerate(FAMILY[sigma])
                       if set(fine)<=set(coarse)) for coarse in FAMILY[pi])
    out={'partition_id':pi,'support_state':record['support_state'],
         'total_weight':record['total_weight'],
         'block_weights':tuple(sum(record['block_weights'][i] for i in indices)
                               for indices in groups),
         'normalized_weight_state':'ZERO_DENOMINATOR'}
    if record['support_state']=='SUPPORTED':
        tag,q=record['normalized_weight_state']
        assert tag=='NORMALIZED'
        out['normalized_weight_state']=('NORMALIZED',tuple(sum(q[i] for i in indices)
                                                       for indices in groups))
    assert coherent_record(out,pi)
    return out


def main():
    assert madd(madd(P0,P1),P2)==ID
    for i,p in enumerate(ATOMS):
        assert sum(p[j][j] for j in range(4))==(1,1,2)[i]
        assert mm(transpose(p),G)==mm(G,p)
        for j,q in enumerate(ATOMS):
            assert mm(p,q)==(p if i==j else ZERO)
    subset_matrices=tuple(pblock(a for a in range(3) if mask&(1<<a)) for mask in range(8))
    assert len({tuple(x for row in p for x in row) for p in subset_matrices})==8
    product_checks,complement_checks=0,0
    for s,p in enumerate(subset_matrices):
        for t,q in enumerate(subset_matrices):
            assert mm(p,q)==subset_matrices[s&t]
            product_checks+=1
        assert madd(ID,mscale(p,-1))==subset_matrices[7^s]
        complement_checks+=1
    assert product_checks==64 and complement_checks==8
    assert generated_partitions((0,1,2))==set(PARTITIONS)
    assert len(FAMILY)==len(PARTITIONS)==5
    coefficient_targets=(outer(E,E,F(1,20)),outer(CHI,CHI,F(1,4)),
                         madd(outer(U,U,F(1,2)),outer(V,V,F(1,2))))
    for p,target in zip(ATOMS,coefficient_targets):
        assert mm(G,p)==target
    for pi in PARTITIONS:
        assert pblock(a for b in pi for a in b)==ID
        for b in pi:
            p=pblock(b)
            assert mm(p,p)==p

    pairs=tuple((sigma,pi) for sigma in PARTITION_IDS for pi in PARTITION_IDS if refines(sigma,pi))
    chains=tuple((sigma,pi,tau) for sigma,pi in pairs for tau in PARTITION_IDS if refines(pi,tau))
    assert len(pairs)==12 and len(chains)==22
    readings,branch_comparisons,coarsening_checks,composition_checks=0,0,0,0
    for values in product(range(-2,3),repeat=4):
        v=tuple(F(x) for x in values)
        col=[[x] for x in v]
        masses=atom_masses(v)
        assert sum(masses)==norm(v) and all(x>=0 for x in masses)
        assert masses[2]==((v[0]-v[3])**2+(v[1]-v[2])**2)/2
        records={}
        for partition_id,pi in FAMILY.items():
            read=passive_vector_read(v,partition_id)
            records[partition_id]=read
            assert coherent_record(read,partition_id)
            if any(v):
                tag,weights=read['normalized_weight_state']
                assert tag=='NORMALIZED' and sum(weights)==1
                for b,weight,raw in zip(pi,weights,read['block_weights']):
                    # Matrix pairing, independent of the closed mass formula.
                    via_matrix=mm(transpose(col),mm(G,mm(pblock(b),col)))[0][0]
                    assert via_matrix/norm(v)==weight and via_matrix==raw
                    branch_comparisons+=1
            else:
                assert read['support_state']=='ZERO_SUPPORT' and read['total_weight']==0
                assert read['block_weights']==(F(0),)*len(pi)
                assert read['normalized_weight_state']=='ZERO_DENOMINATOR'
            readings+=1
        for sigma,pi in pairs:
            assert coarsen(records[sigma],pi)==records[pi]
            coarsening_checks+=1
        for sigma,pi,tau in chains:
            assert coarsen(coarsen(records[sigma],pi),tau)==coarsen(records[sigma],tau)
            composition_checks+=1
    native_records=0
    qr_checks=0
    for head in product(range(5),repeat=6):
        v=tuple((0,1,2,-2,-1)[x] for x in head[:4])
        for partition_id in PARTITION_IDS:
            assert read_head(head,partition_id)==passive_vector_read(v,partition_id)
            native_records+=1
            assert read_head(head,partition_id)==read_head(head[:4]+(0,0),partition_id)
            qr_checks+=1
    assert passive_vector_read((1,0,0,0),'PI-LEG')['normalized_weight_state']==('NORMALIZED',(F(11,16),F(5,16)))
    assert (readings,branch_comparisons,native_records,qr_checks)==(3125,6240,78125,78125)
    assert (coarsening_checks,composition_checks)==(7500,13750)

    # Check the domain on coherent snapshots beyond the finite beta image.
    generic={}
    for sigma,blocks in FAMILY.items():
        w=tuple(F(i+1,7) for i in range(len(blocks)))
        m=sum(w)
        generic[sigma]={'partition_id':sigma,'support_state':'SUPPORTED',
                        'total_weight':m,'block_weights':w,
                        'normalized_weight_state':('NORMALIZED',tuple(x/m for x in w))}
        assert coherent_record(generic[sigma],sigma)
    for sigma,pi in pairs:
        assert coherent_record(coarsen(generic[sigma],pi),pi)
    for sigma,pi,tau in chains:
        assert coarsen(coarsen(generic[sigma],pi),tau)==coarsen(generic[sigma],tau)

    valid=passive_vector_read((1,0,0,0),'PI-TRACE')
    invalid=[]
    for field,value in (
            ('normalized_weight_state','ZERO_DENOMINATOR'),
            ('support_state','ZERO_SUPPORT'),
            ('block_weights',(F(0),)),
            ('total_weight',F(1)),
            ('normalized_weight_state',('NORMALIZED',(F(1,2),F(1,2))))):
        record=dict(valid)
        record[field]=value
        invalid.append(record)
    record=dict(valid)
    record['extra_field']=0
    invalid.append(record)
    for record in invalid:
        assert not coherent_record(record,'PI-TRACE')
        try:
            coarsen(record,'PI-ALL')
        except ValueError:
            pass
        else:
            raise AssertionError('Incoherent record was accepted')
    assert not coherent_record(valid,'PI-LEG')
    try:
        coarsen(valid,'PI-LEG')
    except ValueError:
        pass
    else:
        raise AssertionError('A non-refinement map was accepted')
    assert len(invalid)==6
    report={
        'status':'PUBLIC_PROBE_EXACT_PASSIVE_FAMILY_AUDIT',
        'scope':'chosen algebraic effects and passive weights only',
        'declared_decoder_domain':'K_QDD through existing beta_QDD head factorization',
        'Q4_role':'mathematical extension only',
        'projector_ranks':[1,1,2],
        'boolean_effects':len(subset_matrices),
        'boolean_product_checks':product_checks,
        'boolean_complement_checks':complement_checks,
        'coefficient_matrix_identities':len(coefficient_targets),
        'independently_generated_partitions':len(generated_partitions((0,1,2))),
        'partition_family':FAMILY,
        'balanced_sources_including_zero':625,
        'passive_readings_checked':readings,
        'supported_branch_weight_comparisons':branch_comparisons,
        'native_heads_checked':15625,
        'native_five_field_records_checked':native_records,
        'unused_qr_invariance_checks':qr_checks,
        'refinement_pairs':len(pairs),
        'refinement_chains':len(chains),
        'record_coarsening_equalities':coarsening_checks,
        'record_composition_equalities':composition_checks,
        'coherent_domain_refinement_checks':len(pairs),
        'coherent_domain_composition_checks':len(chains),
        'incoherent_records_rejected':len(invalid),
        'literal_source_id_mismatch_checks':1,
        'non_refinement_rejection_checks':1,
        'not_claimed':['instrument','event occurrence','probability resource','pointer','reset','physical apparatus'],
        'verdict':'PASS',
    }
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
