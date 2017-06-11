from kivy.core.window import Window
from kivy.properties import NumericProperty

from moire.widgets import PanelWidget
from moire.widgets.dlist import DescriptiveList


class SystemInfoWidget(PanelWidget):

    fps = NumericProperty()

    def __init__(self, **kwargs):
        gw, gh = Window.size
        w, h = int(gw * 0.1), int(gh * 0.2)
        kwargs['pos'] = (gw - w - 15, gh - h - 15)
        kwargs['size_hint'] = (None, None)
        kwargs['width'] = w
        kwargs['height'] = h
        super(SystemInfoWidget, self).__init__(**kwargs)
        fields = (
            "FPS",
            "SPS",
            "Speed",
            "Time",
        )
        self.values = DescriptiveList(fields, w)
        self.add_widget(self.values)

    def __setitem__(self, key, value):
        self.values[key] = value
