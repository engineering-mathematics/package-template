"""Behavioural and property-based tests for the template package."""

from __future__ import annotations

import math

import pytest
from hypothesis import given
from hypothesis import strategies as st

from engg_math.template import clamp

finite = st.floats(allow_nan=False, allow_infinity=False, width=64)


@given(value=finite, a=finite, b=finite)
def test_clamp_result_lies_in_interval(value: float, a: float, b: float) -> None:
    low, high = min(a, b), max(a, b)
    assert low <= clamp(value, low, high) <= high


@given(value=finite, a=finite, b=finite)
def test_clamp_is_idempotent(value: float, a: float, b: float) -> None:
    low, high = min(a, b), max(a, b)
    once = clamp(value, low, high)
    assert clamp(once, low, high) == once


def test_clamp_rejects_empty_interval() -> None:
    with pytest.raises(ValueError, match="Empty interval"):
        clamp(0.0, 1.0, -1.0)


@pytest.mark.parametrize("bad", [math.nan])
def test_clamp_rejects_nan(bad: float) -> None:
    with pytest.raises(ValueError, match="NaN"):
        clamp(bad, 0.0, 1.0)
