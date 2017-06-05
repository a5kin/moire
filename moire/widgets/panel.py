from kivy.uix.floatlayout import FloatLayout


class PanelWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(PanelWidget, self).__init__(**kwargs)
        self.bind(pos=self.redraw)
        self.bind(size=self.redraw)

    def redraw(self, *args):
        self.canvas.clear()
