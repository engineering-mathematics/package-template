"""Private implementation. Import from ``engg_math.template``."""

from __future__ import annotations


def clamp(value: float, low: float, high: float) -> float:
    """Return ``value`` limited to ``[low, high]``.

    Raises
    ------
    ValueError
        On NaN input or ``low > high``.
    """
    if value != value or low != low or high != high:  # noqa: PLR0124 - NaN check
        raise ValueError("NaN is not a valid argument")
    if low > high:
        raise ValueError(f"Empty interval: low={low} exceeds high={high}")
    return min(max(value, low), high)
