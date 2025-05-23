"""Define tools such as ``inside_reaper`` and custom json module."""

import renardo_reapy.runtime as runtime
from ._inside_reaper import inside_reaper, dist_api_is_enabled
from .network.machines import connect, connect_to_default_machine, reconnect
from .extension_dependency import depends_on_sws, depends_on_extension
