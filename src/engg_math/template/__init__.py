"""Template package for the Engineering Mathematics ecosystem."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from engg_math.template._core import clamp

try:
    __version__ = version("engg-math-template")
except PackageNotFoundError:  # pragma: no cover - running from an uninstalled checkout
    __version__ = "0.0.0+unknown"

__all__ = ["__version__", "clamp"]
