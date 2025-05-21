"""
Canonical lightweight file I/O.
Only dependency heavier than stdlib is trimesh (already in toolbox env).
"""

from __future__ import annotations
import trimesh, json, pathlib as _pl
from .types import Cap

__all__ = ["load_stl", "save_caps_json", "load_caps_json"]


def load_stl(path: str | _pl.Path, enforce_watertight: bool = True) -> trimesh.Trimesh:
    mesh = trimesh.load(str(path), force="mesh")
    if not isinstance(mesh, trimesh.Trimesh):
        raise ValueError(f"{path!s} did not load to a single mesh")
    if enforce_watertight and not mesh.is_watertight:
        raise ValueError(f"{path!s} is not watertight")
    return mesh


def save_caps_json(caps: list[Cap], path: str | _pl.Path) -> None:
    j = [c.as_dict() for c in caps]
    _pl.Path(path).write_text(json.dumps(j, indent=2))


def load_caps_json(path: str | _pl.Path) -> list[Cap]:
    raw = json.loads(_pl.Path(path).read_text())
    return [Cap.from_dict(d) for d in raw]
