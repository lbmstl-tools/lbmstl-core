"""
Lightweight shared dataclasses for lbmstl-tools.
No heavy imports beyond NumPy and typing.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
import json, typing as tp
import numpy as np

_Array = np.ndarray            # alias to avoid long type hints


def _np_to_list(a: _Array) -> list[float]:
    return a.astype(float).tolist()


@dataclass(slots=True)
class Cap:
    centroid: _Array        # shape (3,)
    normal:   _Array        # shape (3,)  – unit vector
    area:     float
    fid:      int           # original facet index

    # ───── convenience ───────────────────────────────────────────
    def as_dict(self) -> dict[str, tp.Any]:
        d = asdict(self)
        d["centroid"] = _np_to_list(self.centroid)
        d["normal"]   = _np_to_list(self.normal)
        return d

    @classmethod
    def from_dict(cls, d: dict[str, tp.Any]) -> "Cap":
        return cls(
            centroid=np.asarray(d["centroid"], dtype=float),
            normal=np.asarray(d["normal"],   dtype=float),
            area=float(d["area"]),
            fid=int(d["fid"]),
        )


@dataclass(slots=True)
class CenterLine:
    points: _Array          # (N,3)
    lines:  _Array          # VTK connectivity (1-D int32)
    radius: _Array | None = None

    def as_dict(self) -> dict[str, tp.Any]:
        return {
            "points":  self.points.astype(float).tolist(),
            "lines":   self.lines.astype(int).tolist(),
            "radius":  None if self.radius is None else self.radius.tolist(),
        }


@dataclass(slots=True)
class VesselSegment:
    name:   str
    line:   CenterLine
    inlet:  Cap
    outlet: Cap

    def as_dict(self) -> dict[str, tp.Any]:
        return {
            "name":   self.name,
            "line":   self.line.as_dict(),
            "inlet":  self.inlet.as_dict(),
            "outlet": self.outlet.as_dict(),
        }
