"""
The package with the widgets and UI components.

You may use ``widgets`` package as a shortcut to the following
classes.

- ``widgets.PanelWidget`` →
  :class:`moire.widgets.panel.PanelWidget`
- ``widgets.SystemInfoWidget`` →
  :class:`moire.widgets.sysinfo.SystemInfoWidget`
- ``widgets.DescriptiveList`` →
  :class:`moire.widgets.dlist.DescriptiveList`

"""
from moire.widgets.panel import PanelWidget
from moire.widgets.sysinfo import SystemInfoWidget
from moire.widgets.dlist import DescriptiveList

__all__ = [
    "PanelWidget",
    "SystemInfoWidget",
    "DescriptiveList",
]
