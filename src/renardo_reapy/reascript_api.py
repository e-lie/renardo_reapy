import renardo_reapy.runtime as runtime
from renardo_reapy.tools import json, inside_reaper
from renardo_reapy.inside_reaper import is_inside_reaper

import os
import sys


@inside_reaper()
def _get_api_names():
    return __all__


if is_inside_reaper():
    # Import functions without the useless starting "RPR_".
    import reaper_python as _RPR
    __all__ = [s[4:] for s in _RPR.__dict__ if s.startswith("RPR_")]
    for s in __all__:
        exec("{} = _RPR.__dict__['{}']".format(s, "RPR_" + s))

    from renardo_reapy import additional_api as _A_API
    for s in _A_API.__dict__:
        exec("from renardo_reapy.additional_api import {}".format(s))

    # Import SWS functions.
    try:
        sys.path.append(os.path.join(_RPR.RPR_GetResourcePath(), 'Scripts'))
        import sws_python as _SWS
        sws_functions = set(_SWS.__dict__) - set(_RPR.__dict__)
        __all__ += list(sws_functions)
        for s in sws_functions:
            exec("from sws_python import {}".format(s))
    except ImportError:  # SWS is not installed
        pass
else:
    if runtime.dist_api_is_enabled():
        __all__ = _get_api_names()
        func_def = (
            "@inside_reaper()\n"
            "def {name}(*args): return (name)(*args)"
        )
        exec("\n".join(func_def.format(name=name) for name in __all__))
        del func_def
