"""Property-based test examples using Hypothesis.

Hypothesis generates many random inputs to find edge cases automatically.
Delete or adapt these examples for your own code.

See https://hypothesis.readthedocs.io for full documentation.
"""

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st


@pytest.mark.property
@given(st.lists(st.integers()))
def test_list_reverse_is_involution(xs: list[int]) -> None:
    """Reversing a list twice returns the original list."""
    assert list(reversed(list(reversed(xs)))) == xs


@pytest.mark.property
@given(st.text())
def test_string_encode_decode_roundtrip(s: str) -> None:
    """UTF-8 encode/decode is a lossless roundtrip."""
    assert s.encode("utf-8").decode("utf-8") == s


@pytest.mark.property
@given(st.integers(), st.integers())
def test_addition_is_commutative(a: int, b: int) -> None:
    """Addition is commutative: a + b == b + a."""
    assert a + b == b + a


@pytest.mark.property
@given(st.floats(allow_nan=False, allow_infinity=False))
@settings(max_examples=200)
def test_abs_is_non_negative(x: float) -> None:
    """abs() always returns a non-negative value."""
    assert abs(x) >= 0
