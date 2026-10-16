"""Private implementation module. Import from ``engg_math.template`` instead."""

from __future__ import annotations


def clamp(value: float, low: float, high: float) -> float:
    """Restrict ``value`` to the closed interval ``[low, high]``.

    Parameters
    ----------
    value
        The value to restrict.
    low, high
        Interval bounds; ``low`` must not exceed ``high``.

    Returns
    -------
    float
        ``value`` if it lies within the interval, otherwise the nearest bound.

    Raises
    ------
    ValueError
        If ``low > high`` or any argument is NaN.
    """
    if value != value or low != low or high != high:  # noqa: PLR0124 - NaN check
        raise ValueError("NaN is not a valid argument")
    if low > high:
        raise ValueError(f"Empty interval: low={low} exceeds high={high}")
    return min(max(value, low), high)
