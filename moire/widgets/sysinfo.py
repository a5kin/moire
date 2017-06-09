from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from moire.widgets import PanelWidget


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
        self.table = GridLayout(cols=2, pos_hint={'x': 0, 'y': 0},
                                row_force_default=True, row_default_height=40)
        label = Label(text='FPS: ',
                      text_size=(w * 0.3, 0), halign='right')
        self.table.add_widget(label)
        value = Label(text=str(self.fps),
                      text_size=(w * 0.7, 0), halign='left')
        self.table.add_widget(value)
        self.add_widget(self.table)
