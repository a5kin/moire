"""
Main module containing the base class for Moire GUI.

All Moire apps should be ran using :class:`GUI` class. See the example below.

"""
import time
import os
import pkg_resources

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
from kivy.config import Config
from kivy.resources import resource_add_path
from kivy.logger import Logger

from moire.widgets import SystemInfoWidget


Config.set('graphics', 'fullscreen', 'auto')
Config.write()

CUR_DIR = pkg_resources.resource_filename(__name__, "")
resource_add_path(os.path.join(CUR_DIR, "assets/fonts/"))

MAX_FRAME_RATE = 25
FPS_UPDATE_TIME = 0.5


class MainEngine(FloatLayout):
    """
    Class incapsulating main Moire engine functionality.

    :param app:
        :class:`GUI` class instance.

    """

    #: Kivy property containing rendered frames as ``Texture``.
    viewport = ObjectProperty()

    #: Kivy property containing runnable class.
    runnable = ObjectProperty()

    #: Kivy property containing ``Rectangle`` with rendered frames.
    background = ObjectProperty()

    def __init__(self, app, *args, **kwargs):
        """Initialize necessary stuff."""
        super(MainEngine, self).__init__(*args, **kwargs)
        self.sysinfo = SystemInfoWidget()
        self._app = app
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._last_fps_check_time = time.time()
        self._frames_since_last_check = 0
        self._steps_since_last_check = 0

    def prepare(self):
        """Do main preparations before app run."""
        # background for rendering
        self.viewport = Texture.create(size=Window.size)
        self.runnable.set_viewport(Window.size)
        with self.canvas:
            self.background = Rectangle(texture=self.viewport,
                                        pos=(0, 0), size=Window.size)
        # keyboard
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        # system info
        self.add_widget(self.sysinfo)

    def _keyboard_closed(self):
        """Handle keyboard closing."""
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def key_down(self, key):
        """Emulate key down."""
        self._on_keyboard_down(None, (None, key), None, None)

    def _on_keyboard_down(self, *args):
        """Handle key down."""
        keycode = args[1]
        if keycode[1] in self.runnable.bridge.key_actions:
            self.runnable.bridge.key_actions[keycode[1]](self.runnable, self)
        return True

    def update_sysinfo(self):
        """Update System Info widget with actual data."""
        self.sysinfo["time"] = self.runnable.timestep
        self.sysinfo["speed"] = "%dx" % self.runnable.speed
        curtime = time.time()
        time_passed = curtime - self._last_fps_check_time
        if time_passed >= FPS_UPDATE_TIME and self._frames_since_last_check:
            fps = self._frames_since_last_check / time_passed
            sps = self._steps_since_last_check / time_passed
            self.sysinfo["fps"] = "%.2f" % fps
            self.sysinfo["sps"] = "%.2f" % sps
            self._last_fps_check_time = curtime
            self._frames_since_last_check = 0
            self._steps_since_last_check = 0

    def update(self, _dt):
        """Update the whole app, while keeping the frame rate."""
        self.update_sysinfo()
        # remember start time
        start_time = time.time()
        # render the runnable
        buf = self.runnable.render()
        self.viewport.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
        self.background.texture = self.viewport
        # safely run one or several steps
        for i in range(self.runnable.speed):
            self.runnable.step()
            self._steps_since_last_check += 1
            if time.time() - start_time > 1 / MAX_FRAME_RATE:
                spd = max(int(self.runnable.speed / 1.1), i + 1)
                spd -= int(self.runnable.speed == spd and spd > 1)
                self.runnable.speed = spd
                message = "MOIRE: Clock overrun, speed is set to %dx" % spd
                Logger.warning(message)
                break
        self._frames_since_last_check += 1
        # wait until the frame ends if necessary
        if time.time() - start_time < 1 / MAX_FRAME_RATE:
            time.sleep(1 / MAX_FRAME_RATE - time.time() + start_time)
        Clock.schedule_once(self.update)

    def exit_app(self):
        """Exit the app in convenient way."""
        self._app.stop()


class GUI(App):
    """
    Main class for moire GUI.

    Moire apps should be ran with it in following way::

        runnable = YourRunnable()
        gui = moire.GUI(runnable=runnable)
        gui.run()

    The engine is fully relying on your custom runnable class. It
    should implement a number of features like perform a simulation
    step, render frame etc. See the detailed example in the official
    NoiseTV example.

    :param runnable:
        Runnable class, implementing all necessary features.

    """

    def __init__(self, **kwargs):
        """Initialize the GUI."""
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
        self.engine = MainEngine(self)
        super(GUI, self).__init__(**kwargs)

    def build(self):
        """Prepare GUI for running."""
        self.engine.runnable = self.runnable
        self.engine.prepare()
        Clock.schedule_once(self.engine.update)
        return self.engine
