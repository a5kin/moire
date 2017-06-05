from kivy.graphics import Rectangle, Color
from kivy.uix.floatlayout import FloatLayout


class PanelWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(PanelWidget, self).__init__(**kwargs)
        self.bind(pos=self.redraw)
        self.bind(size=self.redraw)
        self.color = (.1, .6, .6)
        self.border_width = 1.5
        self.corner_len = 15
        self.opacity = .85

    def redraw(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(self.color[0] / 2, self.color[1] / 2,
                  self.color[2] / 2, self.opacity)
            Rectangle(pos=self.pos, size=self.size)
