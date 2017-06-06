from kivy.graphics import Rectangle, Color, Line
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.animation import Animation


class PanelWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(PanelWidget, self).__init__(**kwargs)
        self.bind(pos=self.redraw)
        self.bind(x=self.redraw)
        self.bind(y=self.redraw)
        self.bind(size=self.redraw)
        # hardcoded stuff
        self.color = (.1, .6, .6)
        self.border_width = 1
        self.corner_width = 1.5
        self.corner_len = 7
        self.opacity = .85
        # show/hide animations (hardcoded in half)
        self.hidden = True
        self.trans_duration = .3
        self.show_style = "out_bounce"
        self.hide_style = "in_bounce"
        sx, sy = self.pos
        w, h = self.size
        gw, gh = Window.size
        hidden_x = gw + 10
        self.x = hidden_x
        self.show_animation = Animation(x=sx, duration=self.trans_duration,
                                        t=self.show_style)
        self.hide_animation = Animation(x=hidden_x,
                                        duration=self.trans_duration,
                                        t=self.hide_style)

    def toggle(self):
        """ Toggle show/hide the panel with its contents. """
        if self.hidden:
            self.hide_animation.stop(self)
            self.show_animation.start(self)
        else:
            self.show_animation.stop(self)
            self.hide_animation.start(self)
        self.hidden = not self.hidden

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
            print("Redrawing", x, y, w, h)
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
