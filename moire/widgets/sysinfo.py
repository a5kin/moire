from moire.widgets import PanelWidget
from kivy.core.window import Window


class SystemInfoWidget(PanelWidget):

    def __init__(self, **kwargs):
        gw, gh = Window.size
        w, h = int(gw * 0.1), int(gh * 0.2)
        kwargs['pos'] = (gw - w - 15, gh - h - 15)
        kwargs['size'] = (w, h)
        print(w, h)
        super(SystemInfoWidget, self).__init__(**kwargs)
