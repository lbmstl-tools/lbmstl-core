from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version(__name__.replace(".", "-"))
except PackageNotFoundError:   # dev layout
    __version__ = "0.0.0+dev"

from .types import Cap, CenterLine, VesselSegment      # re-export
from .io    import load_stl, save_caps_json, load_caps_json
__all__ = [
    "__version__", "Cap", "CenterLine", "VesselSegment",
    "load_stl", "save_caps_json", "load_caps_json",
]