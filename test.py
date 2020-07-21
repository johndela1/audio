#!/usr/bin/env python3

import math

TOL_MILLI = 10

def correlate(needle, haystack):
    for i in haystack:
        if math.isclose(needle, i, abs_tol=TOL_MILLI):
            return i - needle


def test_correlate():
    delta = correlate(1010, [1000, 2000])
    assert delta
    assert delta == -10

    delta = correlate(1011, [1000, 2000])
    assert delta is None


def correlated(ref, attempt):
    return [correlate(i, ref) for i in attempt]


def test_correlated():
    res = correlated([1000, 2000, 3000, 4000], [1010, 2011, 2989, 2990])
    assert res == [-10, None, None, 10]


test_correlate()
test_correlated()
