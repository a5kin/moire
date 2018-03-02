"""Tests for base Moire stuff."""
import unittest
import time
from functools import partial

from kivy.clock import Clock

import moire
from examples.noisetv import NoiseTV


class TestMainApp(unittest.TestCase):
    """Tests for main app."""

    def pause(*args):
        """Sleep for some time."""
        time.sleep(1)

    def run_test(self, app, *args):
        """Run test itself."""
        Clock.schedule_interval(self.pause, 1)
        self.assertGreater(app.runnable.timestep, 0,
                           "Environment did not run.")
        app.stop()

    def test_example(self):
        """Run the environment and schedule test."""
        environment = NoiseTV()
        app = moire.GUI(runnable=environment)
        p = partial(self.run_test, app)
        Clock.schedule_once(p, 1)
        app.run()
