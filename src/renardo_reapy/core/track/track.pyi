import renardo_reapy.runtime as runtime
from renardo_reapy import reascript_api as RPR
from renardo_reapy.core import ReapyObject, ReapyObjectList
from renardo_reapy.errors import UndefinedEnvelopeError
import typing as ty


class Track(ReapyObject):
    """
    REAPER Track.

    Parameters
    ----------
    id : str or int
        If str, can either be a ReaScript ID (usually looking like
        ``"(MediaTrack*)0x00000000110A1AD0"``), or a track name. In
        that case, ``project`` must be specified.
        If int, the index of the track. In that case, ``project`` must
        be specified.
    project : Project
        Parent project of the track. Only necessary to retrieve a
        track from its name or index.

    Examples
    --------
    In most cases, accessing tracks is better done directly from
    the parent Project:

    >>> project = renardo_reapy.Project()
    >>> project.tracks[0]
    Track("(MediaTrack*)0x00000000110A1AD0")
    >>> project.tracks["PIANO"]  # This is actually the same track
    Track("(MediaTrack*)0x00000000110A1AD0")

    But the same track can also directly be instantiated with:

    >>> renardo_reapy.Track(0, project)
    Track("(MediaTrack*)0x00000000110A1AD0")

    or

    >>> renardo_reapy.Track("PIANO")
    Track("(MediaTrack*)0x00000000110A1AD0")
    """
    id: str
    _project: renardo_reapy.Project

    def __init__(
        self,
        id: ty.Union[str, int, float],
        project: ty.Optional[renardo_reapy.Project] = None
    ) -> None:
        ...

    @property
    def _args(self) -> ty.Tuple[ty.Union[str, int]]:
        ...

    @classmethod
    def _get_id_from_pointer(cls, id_: ty.Union[int, float]) -> str:
        ...

    def _get_project(self) -> renardo_reapy.Project:
        """
        Return parent project of track.

        Should only be used internally; one should directly access
        Track.project instead of calling this method.
        """
        ...

    def add_audio_accessor(self) -> renardo_reapy.AudioAccessor:
        """
        Create audio accessor and return it.

        Returns
        -------
        audio_accessor : AudioAccessor
            Audio accessor on track.
        """
        ...

    def add_fx(
        self, name: str, input_fx: bool = False, even_if_exists: bool = True
    ) -> renardo_reapy.FX:
        """
        Add FX to track and return it.

        Parameters
        ----------
        name : str
            FX name.
        input_fx : bool, optional
            Whether the FX should be an input (aka recording) FX or a
            standard FX (default=False). Note that if the track is the
            master track, input_fx=True will create a monitoring FX.
        even_if_exists : bool, optional
            Whether the FX should be added even if there already is an
            instance of the same FX on the track (default=True).

        Returns
        -------
        fx : FX
            New FX on track (or previously existing instance of FX if
            even_if_exists=False).

        Raises
        ------
        ValueError
            If there is no FX with the specified name.
        """
        ...

    def add_item(
        self,
        start: float = 0,
        end: ty.Optional[float] = None,
        length: float = 0
    ) -> renardo_reapy.Item:
        """
        Create new item on track and return it.

        Parameters
        ----------
        start : float, optional
            New item start in seconds (default=0).
        end : float, optional
            New item end in seconds (default None). If None, `length`
            is used instead.
        length : float, optional
            New item length in seconds (default 0).

        Returns
        -------
        item : Item
            New item on track.
        """
        ...

    def add_midi_item(
        self, start: float = 0, end: float = 1, quantize: bool = False
    ) -> renardo_reapy.Item:
        """
        Add empty MIDI item to track and return it.

        Parameters
        ----------
        start : float, optional
            New item start in seconds (or beats if `quantize`=True).
        end : float, optional
            New item end in seconds (or beats if `quantize`=True).
        quantize : bool, optional
            Whether to count time in beats (True) or seconds (False,
            default).
        """
        ...

    def add_send(
        self, destination: ty.Optional[renardo_reapy.Track] = None
    ) -> renardo_reapy.Send:
        """
        Add send to track and return it.

        Parameters
        ----------
        destination : Track or None
            Send destination (default=None). If None, destination is
            set to hardware output.

        Returns
        -------
        send : Send
            New send on track.
        """
        ...

    @property
    def automation_mode(self) -> str:
        """
        Track automation mode.

        One of the following values:
            "latch"
            "latch preview"
            "read"
            "touch"
            "trim/read"
            "write"

        :type: str
        """
        ...

    @automation_mode.setter
    def automation_mode(self, mode: str) -> None:
        """
        Set track automation mode.

        Parameters
        -------
        mode : str
            One of the following values:
                "latch"
                "latch preview"
                "read"
                "touch"
                "trim/read"
                "write"
        """
        ...

    @property
    def color(self) -> ty.Tuple[int, int, int]:
        """
        Track color in RGB format.

        :type: tuple of int
        """
        ...

    @color.setter
    def color(self, color: ty.Tuple[int, int, int]) -> None:
        """
        Set track color to `color`

        Parameters
        ----------
        color : tuple
            Triplet of integers between 0 and 255 corresponding to RGB
            values.
        """
        ...

    def delete(self) -> None:
        """
        Delete track.
        """
        ...

    @property
    def depth(self) -> int:
        """
        Track depth.

        :type: int
        """
        ...

    @property
    def envelopes(self) -> renardo_reapy.EnvelopeList:
        """
        List of envelopes on track.

        :type: EnvelopeList
        """
        ...

    @property
    def fxs(self) -> renardo_reapy.FXList:
        """
        List of FXs on track.

        :type: FXList
        """
        ...

    def get_info_string(self, param_name: str) -> str:
        ...

    def get_info_value(self, param_name: str) -> float:
        ...

    @property
    def GUID(self) -> str:
        """
        Track's GUID.

        16-byte GUID, can query or update.
        If using a _String() function, GUID is a string {xyz-...}.

        :type: str
        """
        ...

    @GUID.setter
    def GUID(self, guid_string: str) -> None:
        ...

    @property
    def has_valid_id(self) -> bool:
        """
        Whether ReaScript ID is still valid.

        For instance, if track has been deleted, ID will not be valid
        anymore.

        :type: bool
        """

    @property
    def icon(self) -> str:
        """
        Track icon.

        Full filename, or relative to resource_path/data/track_icons.

        :type: str
        """
        ...

    @icon.setter
    def icon(self, filename: str) -> None:
        ...

    @property
    def index(self) -> ty.Optional[int]:
        """
        Track index in GUI (0-based).

        Will be ``None`` for master track.

        :type: int or None

        Raises
        ------
        InvalidObjectError
            When track does not exist in REAPER.
        """
        ...

    @property
    def instrument(self) -> ty.Optional[renardo_reapy.FX]:
        """
        First instrument FX on track if it exists, else None.

        :type: FX or None
        """
        ...

    @property
    def items(self) -> ty.List[renardo_reapy.Item]:
        """
        List of items on track.

        :type: list of Item
        """
        ...

    @property
    def is_muted(self) -> bool:
        """
        Whether track is muted.

        Can be manually set to change track state.
        """
        ...

    @is_muted.setter
    def is_muted(self, muted: bool) -> None:
        ...

    @property
    def is_selected(self) -> bool:
        """
        Whether track is selected.

        :type: bool
        """
        ...

    @is_selected.setter
    def is_selected(self, selected: bool) -> None:
        """
        Select or unselect track.

        Parameters
        ----------
        selected : bool
            Whether to select or unselect track.
        """
        ...

    @property
    def is_solo(self) -> bool:
        """
        Whether track is solo.

        Can be manually set to change track state.
        """
        ...

    @is_solo.setter
    def is_solo(self, solo: bool) -> None:
        ...

    def make_only_selected_track(self) -> None:
        """
        Make track the only selected track in parent project.
        """
        ...

    def midi_hash(self, notes_only: bool = False) -> str:
        """Get hash of MIDI-data to compare with later.

        Parameters
        ----------
        notes_only : bool, (False by default)
            count only notes if True

        Returns
        -------
        str
        """
        ...

    @property
    def midi_note_names(self) -> ty.List[str]:
        ...

    def mute(self) -> None:
        """Mute track (do nothing if track is already muted)."""
        ...

    @property
    def n_envelopes(self) -> int:
        """
        Number of envelopes on track.

        :type: int
        """
        ...

    @property
    def n_fxs(self) -> int:
        """
        Number of FXs on track.

        :type: int
        """
        ...

    @property
    def n_hardware_sends(self) -> int:
        """
        Number of hardware sends on track.

        :type: int
        """
        ...

    @property
    def n_items(self) -> int:
        """
        Number of items on track.

        :type: int
        """
        ...

    @property
    def n_receives(self) -> int:
        ...

    @property
    def n_sends(self) -> int:
        ...

    @property
    def name(self) -> str:
        """
        Track name.

        Name is "MASTER" for master track, "Track N" if track has no
        name.

        :type: str
            Track name .
        """
        ...

    @name.setter
    def name(self, track_name: str) -> None:
        ...

    @property
    def parent_track(self) -> ty.Optional[renardo_reapy.Track]:
        """
        Parent track, or None if track has none.

        :type: Track or NoneType
        """
        ...

    @property
    def project(self) -> renardo_reapy.Project:
        """
        Track parent project.

        :type: Project
        """
        ...

    @property
    def receives(self) -> ty.List[renardo_reapy.Send]: ...

    def select(self) -> None:
        """
        Select track.
        """
        ...

    @property
    def sends(self) -> ty.List[renardo_reapy.Send]:
        ...

    def set_info_string(self, param_name: str, param_string: str) -> None:
        ...

    def set_info_value(self, param_name: str, param_value: float) -> None: ...

    def solo(self) -> None:
        """Solo track (do nothing if track is already solo)."""
        ...

    def toggle_mute(self) -> None:
        """Toggle mute on track."""
        ...

    def toggle_solo(self) -> None:
        """Toggle solo on track."""
        ...

    def unmute(self) -> None:
        """Unmute track (do nothing if track is not muted)."""
        ...

    def unselect(self) -> None:
        """
        Unselect track.
        """
        ...

    def unsolo(self) -> None:
        """Unsolo track (do nothing if track is not solo)."""
        ...

    @property
    def visible_fx(self) -> renardo_reapy.FX:
        """
        Visible FX in FX chain if any, else None.

        :type: FX or NoneType
        """
        ...


class TrackList(ReapyObjectList):
    """
    Container for a project's track list.

    Examples
    --------
    >>> tracks = project.tracks
    >>> len(tracks)
    4
    >>> tracks[0].name
    'Kick'
    >>> for track in tracks:
    ...     print(track.name)
    ...
    'Kick'
    'Snare'
    'Hi-hat'
    'Cymbal"
    """
    parent: renardo_reapy.Project

    def __init__(self, parent: renardo_reapy.Project) -> None:
        """
        Create track list.

        Parameters
        ----------
        parent : Project
            Parent project.
        """
        ...

    @ty.overload
    def __getitem__(self, key: str) -> Track:
        ...

    @ty.overload
    def __getitem__(self, key: int) -> Track:
        ...

    @ty.overload
    def __getitem__(self, key: slice) -> ty.List[Track]:
        ...

    def __delitem__(self, key: ty.Union[int, slice]) -> None:
        ...

    def __len__(self) -> int:
        ...

    def __iter__(self) -> ty.Iterator[renardo_reapy.Track]:
        ...

    @property
    def _args(self) -> ty.Tuple[renardo_reapy.Project]:
        ...

    def _get_items_from_slice(self, slice: slice) -> ty.List[Track]:
        ...
