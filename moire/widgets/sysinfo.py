from kivy.core.window import Window
from kivy.properties import NumericProperty

from moire.widgets import PanelWidget
from moire.widgets.dlist import DescriptiveList


class SystemInfoWidget(PanelWidget):

    fps = NumericProperty()

    def __init__(self, **kwargs):
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
        self.values[key] = value
