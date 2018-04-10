"""Module with the base ``Panel`` class."""
from kivy.graphics import Rectangle, Color, Line
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.animation import Animation


class PanelWidget(FloatLayout):
    """
    The implementation of the base panel widget.

    Other widgets could be inherited from ``Panel`` in order to get
    the standard visual decoration and show/hide transitions.

    """

    def __init__(self, **kwargs):
        """Initialize the widget and its state variables."""
        super(PanelWidget, self).__init__(**kwargs)
        self.bind(pos=self.redraw)
        self.bind(size=self.redraw)
        # hardcoded stuff
        self.color = (.1, .6, .6)
        self.border_width = 1
        self.corner_width = 1.5
        self.corner_len = 7
        self.opacity = .85
        # show/hide animations (hardcoded in half)
        self.hidden = True
        self.trans_duration_in = .6
        self.trans_duration_out = .3
        self.show_style = "out_elastic"
        self.hide_style = "in_back"
        scroll_x = self.pos[0]
        global_w = Window.size[0]
        hidden_x = global_w + 10
        self.x = hidden_x
        self.show_animation = Animation(x=scroll_x,
                                        duration=self.trans_duration_in,
                                        t=self.show_style)
        self.hide_animation = Animation(x=hidden_x,
                                        duration=self.trans_duration_out,
                                        t=self.hide_style)

    def toggle(self):
        """Toggle show/hide the panel with its contents."""
        if self.hidden:
            self.hide_animation.stop(self)
            self.show_animation.start(self)
        else:
            self.show_animation.stop(self)
            self.hide_animation.start(self)
        self.hidden = not self.hidden

    def redraw(self, *_args):
        """Redraw panel on the canvas."""
        saved_children = self.children[:]
        self.clear_widgets()
        self.canvas.clear()
        with self.canvas:
            # background
            Color(self.color[0] / 2, self.color[1] / 2,
                  self.color[2] / 2, self.opacity)
            Rectangle(pos=self.pos, size=self.size)
            # border
            Color(self.color[0], self.color[1],
                  self.color[2], 1)
            pos_x, pos_y = self.pos
            width, height = self.size
            Line(points=[pos_x, pos_y, pos_x + width,
                         pos_y, pos_x + width,
                         pos_y + height, pos_x,
                         pos_y + height, pos_x, pos_y],
                 width=self.border_width,
                 cap='square', joint='miter')
            # corners
            Color(1, 1, 1, .7)
            Line(points=[pos_x + self.corner_len, pos_y,
                         pos_x, pos_y,
                         pos_x, pos_y + self.corner_len],
                 width=self.corner_width,
                 cap='square', joint='miter')
            Line(points=[pos_x + width - self.corner_len,
                         pos_y, pos_x + width, pos_y,
                         pos_x + width, pos_y + self.corner_len],
                 width=self.corner_width,
                 cap='square', joint='miter')
            Line(points=[pos_x, pos_y + height - self.corner_len,
                         pos_x, pos_y + height,
                         pos_x + self.corner_len, pos_y + height],
                 width=self.corner_width,
                 cap='square', joint='miter')
            Line(points=[pos_x + width, pos_y + height - self.corner_len,
                         pos_x + width, pos_y + height,
                         pos_x + width - self.corner_len, pos_y + height],
                 width=self.corner_width,
                 cap='square', joint='miter')
        for widget in saved_children:
            self.add_widget(widget)
