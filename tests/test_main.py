"""Tests for base Moire stuff."""
import unittest
from functools import partial

from kivy.clock import Clock

import moire
from examples.noisetv import NoiseTV


class TestMainApp(unittest.TestCase):
    """Tests for main app."""

    def pause(*args):
        """Sleep for some time."""

    def check_run(self, app, *args):
        """Check app is running."""
        self.assertGreater(app.runnable.timestep, 0,
                           "Environment did not run.")

    def press_key(self, key):
        """Emulate key pressing."""
        self.app.engine._on_keyboard_down(None, (None, key), None, None)

    def stop_app(self, app, *args):
        """Stop main application."""
        self.press_key("escape")

    def increase_speed(self, app, *args):
        """Speed emulation up."""
        app.runnable.apply_speed(23)

    def decrease_speed(self, app, *args):
        """Speed emulation dowd."""
        self.assertGreater(app.runnable.speed, 1,
                           "Speed has not increased.")
        app.runnable.apply_speed(-23)
        self.assertEqual(app.runnable.speed, 1,
                         "Speed has not decreased.")

    def toggle_sysinfo(self, app, *args):
        """Show/hide system info panel."""
        app.engine.sysinfo.toggle()

    def schedule(self, action, time_sec):
        """Schedule ``action`` function at ``time``."""
        p = partial(action, self.app)
        Clock.schedule_once(p, time_sec)

    def test_windowed(self):
        """Run the windowed environment and schedule test actions."""
        environment = NoiseTV()
        self.app = moire.GUI(runnable=environment, size=(640, 480))
        self.schedule(self.check_run, 1)
        self.schedule(self.increase_speed, 1.2)
        self.schedule(self.decrease_speed, 2.5)
        self.schedule(self.toggle_sysinfo, 1)
        self.schedule(self.toggle_sysinfo, 2)
        self.schedule(self.stop_app, 3)
        self.app.run()

    def test_fullscreen(self):
        """Run the environment fullscreen."""
        environment = NoiseTV()
        self.app = moire.GUI(runnable=environment)
        self.schedule(self.stop_app, 1)
        self.app.run()

    def test_illegal(self):
        """Run the environment without runnable."""
        with self.assertRaises(ValueError):
            self.app = moire.GUI()
            self.schedule(self.stop_app, 1)
            self.app.run()
