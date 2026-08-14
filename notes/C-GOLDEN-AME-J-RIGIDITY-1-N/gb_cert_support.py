#!/usr/bin/env python3
"""Small standard-library support layer for the frozen-order certificate."""

from __future__ import annotations

from fractions import Fraction
from functools import reduce
from math import gcd
import hashlib
import importlib.util
from pathlib import Path
import sys


BUILDER_SHA256 = "b26844a99db5ff9baf4ed7493ed8c9c7aea28a561c8eeadb2c70fdc77530383c"
RAW_SHA256 = "09aac23466680ba762e363ad75845aa1535f4e8e32cee75ad41119f43cb16762"


def load_builder(path: Path):
    data = path.read_bytes()
    assert hashlib.sha256(data).hexdigest() == BUILDER_SHA256
    spec = importlib.util.spec_from_file_location("golden_symbolic_frozen_verify", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def clean(polynomial):
    return {monomial: coefficient for monomial, coefficient in polynomial.items()
            if coefficient}


def add(left, right, scale=Fraction(1)):
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, Fraction(0)) + scale * coefficient
    return clean(result)


def mul(left, right):
    result = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(a + b for a, b in zip(left_monomial, right_monomial))
            result[monomial] = (
                result.get(monomial, Fraction(0))
                + left_coefficient * right_coefficient
            )
    return clean(result)


def monomial_poly(monomial, coefficient=Fraction(1)):
    return {} if not coefficient else {tuple(monomial): coefficient}


def lm(polynomial):
    return max(polynomial)


def divides(left, right):
    return all(a <= b for a, b in zip(left, right))


def divide_remainder(polynomial, basis):
    work, remainder = dict(polynomial), {}
    while work:
        monomial = lm(work)
        coefficient = work[monomial]
        for divisor in basis:
            divisor_monomial = lm(divisor)
            if divides(divisor_monomial, monomial):
                quotient_monomial = tuple(
                    a - b for a, b in zip(monomial, divisor_monomial)
                )
                quotient = monomial_poly(
                    quotient_monomial, coefficient / divisor[divisor_monomial]
                )
                work = add(work, mul(quotient, divisor), Fraction(-1))
                break
        else:
            remainder[monomial] = coefficient
            del work[monomial]
    return clean(remainder)


def spoly(left, right):
    left_monomial, right_monomial = lm(left), lm(right)
    common = tuple(max(a, b) for a, b in zip(left_monomial, right_monomial))
    left_multiplier = tuple(a - b for a, b in zip(common, left_monomial))
    right_multiplier = tuple(a - b for a, b in zip(common, right_monomial))
    normalized_left = mul(
        monomial_poly(left_multiplier, Fraction(1) / left[left_monomial]), left
    )
    normalized_right = mul(
        monomial_poly(right_multiplier, Fraction(1) / right[right_monomial]), right
    )
    return add(normalized_left, normalized_right, Fraction(-1))


def parse_poly(serialized):
    return clean({
        tuple(monomial): Fraction(numerator, denominator)
        for monomial, numerator, denominator in serialized
    })


def normalize_key(polynomial):
    terms = {monomial: coefficient for monomial, coefficient in polynomial.items()
             if coefficient}
    if not terms:
        return ()
    content = reduce(gcd, (abs(coefficient) for coefficient in terms.values()))
    terms = {monomial: coefficient // content
             for monomial, coefficient in terms.items()}
    # Frozen order is alpha > beta > gamma > y > x, while the source stores
    # the last two exponents as x,y.
    leading = max(terms, key=lambda m: (m[0], m[1], m[2], m[4], m[3]))
    if terms[leading] < 0:
        terms = {monomial: -coefficient
                 for monomial, coefficient in terms.items()}
    return tuple(sorted(terms.items()))


def regenerate_inputs(source: Path, block944: Path, builder: Path):
    module = load_builder(builder)
    source_bytes = source.read_bytes()
    block_bytes = block944.read_bytes()
    module.verify_pin(source_bytes, module.ORIGINAL_PIN)
    module.verify_pin(block_bytes, module.BLOCK944_PIN)
    assert module.parse_block944_permutations(block_bytes) == (
        module.BLOCK_ROW_TO_G_ROW, module.BLOCK_COL_TO_G_COL
    )
    tensor = module.construct_a_direct(source_bytes)
    assert tensor == module.construct_b_blocks()
    equations = module.gram_equations(tensor)
    raw_bytes = module.serialize_equations(equations)
    assert len(equations) == 3889
    assert sum(bool(equation.polynomial) for equation in equations) == 383
    assert len(raw_bytes) == 136262
    raw_sha256 = hashlib.sha256(raw_bytes).hexdigest()
    assert raw_sha256 == RAW_SHA256

    unique = sorted({normalize_key(equation.polynomial) for equation in equations} - {()})
    inputs = []
    for key in unique:
        polynomial = {}
        for (alpha, beta, gamma, x, y), coefficient in key:
            polynomial[(0, alpha, beta, gamma, y, x)] = Fraction(coefficient)
        inputs.append(polynomial)
    # Sole frozen Rabinowitsch generator, in t,alpha,beta,gamma,y,x order.
    inputs.append({
        (0, 0, 0, 0, 0, 0): Fraction(1),
        (1, 1, 1, 1, 1, 1): Fraction(-1),
    })
    return inputs, raw_sha256
