from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.config import Config


Config.set('graphics', 'fullscreen', 'auto')
Config.write()


class MainEngine(Widget):

    def update(self, dt):
        pass


class GUI(App):

    def __init__(self, **kwargs):
        if 'runnable' in kwargs:
            self.runnable = kwargs['runnable']
            del kwargs['runnable']
        else:
            raise ValueError("Missing ``runnable`` from argument list.")
        # FIXME: side effect, sets windowed/fullscreen mode only on next run
        if 'size' in kwargs:
            Config.set('graphics', 'fullscreen', '0')
            Config.write()
            self.size = kwargs['size']
            del kwargs['size']
        else:
            self.size = Window.size
        Window.size = self.size
        super(GUI, self).__init__(**kwargs)

    def build(self):
        engine = MainEngine()
        Clock.schedule_interval(engine.update, 1.0 / 25.0)
        return engine
