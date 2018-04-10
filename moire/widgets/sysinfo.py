"""Module for widget with system info."""
from kivy.core.window import Window
from kivy.properties import NumericProperty

from moire.widgets import PanelWidget
from moire.widgets.dlist import DescriptiveList


class SystemInfoWidget(PanelWidget):
    """
    Build-in widget showing system info.

    The fields are:

       FPS
          Current frames per second speed (for GUI).
       SPS
          Current steps per second speed (for simulation).
       Speed
          How many steps are skipped each frame.
       Time
          Global timestep counter.

    """

    #: Desired frame rate
    fps = NumericProperty()

    def __init__(self, **kwargs):
        """Initialize widget."""
        global_w, global_h = Window.size
        width, height = int(global_w * 0.115), int(global_h * 0.08)
        kwargs['pos'] = (global_w - width - 15, global_h - height - 15)
        kwargs['size_hint'] = (None, None)
        kwargs['width'] = width
        kwargs['height'] = height
        super(SystemInfoWidget, self).__init__(**kwargs)
        fields = (
            "FPS",
            "SPS",
            "Speed",
            "Time",
        )
        self.values = DescriptiveList(fields, width, height / 5)
        self.add_widget(self.values)

    def __setitem__(self, key, value):
        """Set value by key at runtime."""
        self.values[key] = value
