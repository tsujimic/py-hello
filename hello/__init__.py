from ._version import VERSION, SDK_MONIKER
from ._hello import format_as_ndjson

__version__ = VERSION

__all__ = (
    "SDK_MONIKER",
    "VERSION",
    "format_as_ndjson",
)