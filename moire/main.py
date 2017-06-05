import time

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
from kivy.config import Config

from moire.widgets import SystemInfoWidget


Config.set('graphics', 'fullscreen', 'auto')
Config.write()

FRAME_RATE = 25


class MainEngine(FloatLayout):

    viewport = ObjectProperty()
    runnable = ObjectProperty()
    background = ObjectProperty()

    def prepare(self):
        # background for rendering
        self.viewport = Texture.create(size=Window.size)
        self.runnable.set_viewport(Window.size)
        with self.canvas:
            self.background = Rectangle(texture=self.viewport,
                                        pos=(0, 0), size=Window.size)
        # keyboard
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        # system info
        self.sysinfo = SystemInfoWidget(size_hint=(.2, .2),
                                        pos_hint={"y": .75, "x": .75})
        self.add_widget(self.sysinfo)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] in self.runnable.bridge.key_actions:
            self.runnable.bridge.key_actions[keycode[1]](self.runnable, self)
        return True

    def update(self, dt):
        # remember start time
        start_time = time.time()
        # render the runnable
        buf = self.runnable.render()
        self.viewport.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
        self.background.texture = self.viewport
        # safely run one or several steps
        for i in range(self.runnable.speed):
            self.runnable.step()
            if time.time() - start_time > 1 / FRAME_RATE:
                break
        # wait until the frame ends if necessary
        if time.time() - start_time < 1 / FRAME_RATE:
            time.sleep(1 / FRAME_RATE - time.time() + start_time)
        Clock.schedule_once(self.update)

    def exit_app(self):
        app = App.get_running_app()
        app.stop()


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
        engine.runnable = self.runnable
        engine.prepare()
        Clock.schedule_once(engine.update)
        return engine
