from kivy.graphics import Rectangle, Color, Line
from kivy.uix.floatlayout import FloatLayout


class PanelWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(PanelWidget, self).__init__(**kwargs)
        self.bind(pos=self.redraw)
        self.bind(size=self.redraw)
        # hardcoded stuff
        self.color = (.1, .6, .6)
        self.border_width = 1
        self.corner_width = 1.5
        self.corner_len = 7
        self.opacity = .85

    def redraw(self, *args):
        """ Redraw panel on the canvas. """
        self.canvas.clear()
        with self.canvas:
            # background
            Color(self.color[0] / 2, self.color[1] / 2,
                  self.color[2] / 2, self.opacity)
            Rectangle(pos=self.pos, size=self.size)
            # border
            Color(self.color[0], self.color[1],
                  self.color[2], 1)
            x, y = self.pos
            w, h = self.size
            Line(points=[x, y, x + w, y, x + w,
                         y + h, x, y + h, x, y],
                 width=self.border_width,
                 cap='square', joint='miter')
            # corners
            Color(1, 1, 1, .7)
            Line(points=[x + self.corner_len, y, x, y,
                         x, y + self.corner_len],
                 width=self.corner_width,
                 cap='square', joint='miter')
            Line(points=[x + w - self.corner_len, y, x + w, y,
                         x + w, y + self.corner_len],
                 width=self.corner_width,
                 cap='square', joint='miter')
            Line(points=[x, y + h - self.corner_len, x, y + h,
                         x + self.corner_len, y + h],
                 width=self.corner_width,
                 cap='square', joint='miter')
            Line(points=[x + w, y + h - self.corner_len, x + w, y + h,
                         x + w - self.corner_len, y + h],
                 width=self.corner_width,
                 cap='square', joint='miter')
