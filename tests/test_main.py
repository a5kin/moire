"""Tests for base Moire stuff."""
import unittest

from kivy.clock import Clock

import moire
from examples.noisetv import NoiseTV


class TestMainApp(unittest.TestCase):
    """Tests for main app."""

    def __init__(self, *args, **kwargs):
        """Initialize test."""
        super(TestMainApp, self).__init__(*args, **kwargs)
        self.app = None

    def check_run(self, *_):
        """Check app is running."""
        self.assertGreater(self.app.runnable.timestep, 0,
                           "Environment did not run.")

    def press_key(self, key):
        """Emulate key pressing."""
        self.app.engine.key_down(key)

    def stop_app(self, *_):
        """Stop main application."""
        self.press_key("escape")

    def increase_speed(self, *_):
        """Speed emulation up."""
        self.app.runnable.apply_speed(23)

    def decrease_speed(self, *_):
        """Speed emulation dowd."""
        self.assertGreater(self.app.runnable.speed, 1,
                           "Speed has not increased.")
        self.app.runnable.apply_speed(-23)
        self.assertEqual(self.app.runnable.speed, 1,
                         "Speed has not decreased.")

    def toggle_sysinfo(self, *_):
        """Show/hide system info panel."""
        self.app.engine.sysinfo.toggle()

    def test_windowed(self):
        """Run the windowed environment and schedule test actions."""
        environment = NoiseTV()
        self.app = moire.GUI(runnable=environment, size=(640, 480))
        Clock.schedule_once(self.check_run, 1)
        Clock.schedule_once(self.increase_speed, 1.2)
        Clock.schedule_once(self.decrease_speed, 2.5)
        Clock.schedule_once(self.toggle_sysinfo, 1)
        Clock.schedule_once(self.toggle_sysinfo, 2)
        Clock.schedule_once(self.stop_app, 3)
        self.app.run()

    def test_fullscreen(self):
        """Run the environment fullscreen."""
        environment = NoiseTV()
        self.app = moire.GUI(runnable=environment)
        Clock.schedule_once(self.stop_app, 1)
        self.app.run()

    def test_illegal(self):
        """Run the environment without runnable."""
        with self.assertRaises(ValueError):
            self.app = moire.GUI()
            Clock.schedule_once(self.stop_app, 1)
            self.app.run()
