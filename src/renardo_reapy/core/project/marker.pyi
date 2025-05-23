import renardo_reapy.runtime as runtime
from renardo_reapy import reascript_api as RPR
from renardo_reapy.core import ReapyObject
import typing as ty


class Marker(ReapyObject):

    _class_name = "Marker"
    project: renardo_reapy.Project
    project_id: int
    index: int

    def __init__(self,
                 parent_project: ty.Optional[renardo_reapy.Project] = None,
                 index: ty.Optional[int] = None,
                 parent_project_id: ty.Optional[int] = None):
        ...

    @inside_reaper()
    def _get_enum_index(self) -> int:
        """
        Return marker index as needed by RPR.EnumProjectMarkers2.
        """
        ...

    @property
    def _kwargs(self) -> ty.Dict[str, int]:
        ...

    def delete(self) -> None:
        """
        Delete marker.
        """
        ...

    @property
    def position(self) -> float:
        """
        Return marker position.

        Returns
        -------
        position : float
            Marker position in seconds.
        """
        ...

    @position.setter
    def position(self, position: float) -> None:
        """
        Set marker position.

        Parameters
        ----------
        position : float
            Marker position in seconds.
        """
        ...
