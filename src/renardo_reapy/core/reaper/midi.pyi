import renardo_reapy.runtime as runtime
import renardo_reapy.reascript_api as RPR
import typing as ty


def get_active_editor() -> ty.Optional[renardo_reapy.MIDIEditor]:
    """
    Return active MIDI editor, or None if no editor is active.

    Returns
    -------
    editor : MIDIEditor or None
        Active MIDI editor, or None if no editor is active.
    """
    ...


@inside_reaper()
def get_input_names() -> ty.List[str]:
    """
    Return names of all input channels.

    Returns
    -------
    names : list of str
        Names of input channels.
    """
    ...


def get_max_inputs() -> int:
    """
    Return maximum number of MIDI inputs.

    Returns
    -------
    max_inputs : int
        Maximum number of MIDI inputs.
    """
    ...


def get_max_outputs() -> int:
    """
    Return maximum number of MIDI outputs.

    Returns
    -------
    max_outputs : int
        Maximum number of MIDI outputs.
    """
    ...


def get_n_inputs() -> int:
    """
    Return number of MIDI inputs.

    Returns
    -------
    n_inputs : int
        Number of MIDI inputs.
    """
    ...


def get_n_outputs() -> int:
    """
    Return number of MIDI outputs.

    Returns
    -------
    n_outputs : int
        Number of MIDI outputs.
    """
    ...


@inside_reaper()
def get_output_names() -> ty.List[str]:
    """
    Return names of all output channels.

    Returns
    -------
    names : list of str
        Names of output channels.
    """
    ...


def reinit() -> None:
    """Reset all MIDI devices."""
    ...
