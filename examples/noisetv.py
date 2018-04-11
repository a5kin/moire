"""
The example showing how to build an environment runnable with Moire.

We will set up Noise TV environment, which is generating a
preudorandom array each step, then render it to a viewport as
necessary.

"""

import numpy as np

import moire


class NoiseTV:
    """
    Welcome to the Noise TV.

    You will find nothing but a pseudorandom noise here, 24/7. Just
    relax, stare at the screen for some time, and your imagination
    could start playing games with you.

    """

    def __init__(self):
        """
        Initialize the environment.

        Some attributes are mandatory for this class, since Moire is
        relying on them:

        ``timestep``
            A positive integer, holding current time step number. You
            must properly increment it in ``step()`` method.
        ``speed``
            An integer >= 1, representing the simulation speed, or
            exactly the number of steps per visualization frame.
        ``paused``
            A flag showing if simulation is paused or running.
        ``bridge``
            A bridge class between Moire and your environment.

        """
        self._size = 3
        self._screen = np.zeros((self._size, ), dtype=np.uint8)
        self.timestep = 0
        self.speed = 1
        self.paused = False
        self.bridge = MoireBridge

    def set_viewport(self, size):
        """
        Set viewport (camera) size and initialize array for it.

        :param size: tuple with width and height in pixels.

        """
        self._size = size[0] * size[1] * 3
        self._screen = np.zeros((self._size, ), dtype=np.uint8)

    def apply_speed(self, dval):
        """
        Change the simulation speed.

        :param dval: Delta by which speed is changed.

        """
        self.speed = max(1, (self.speed + dval))

    def toggle_pause(self):
        """
        Toggle ``paused`` flag.

        When paused, the ``step()`` method does nothing.

        """
        self.paused = not self.paused

    def step(self):
        """
        Perform a single simulation step.

        ``timestep`` attribute will hold the current step number.

        """
        if self.paused:
            return
        self._screen = np.random.randint(0, 255, (self._size, ),
                                         dtype=np.uint8)
        self.timestep += 1

    def render(self):
        """
        Render the field at the current timestep.

        You must call :meth:`set_viewport` before do any rendering.

        :returns:
            NumPy array of ``np.uint8`` values, ``width * height * 3``
            size. The RGB values are consecutive.

        """
        return self._screen


class Bridge:
    """Main bridge class containing basic functions."""

    @staticmethod
    def exit_app(_env, gui):
        """Exit GUI application."""
        gui.exit_app()

    @staticmethod
    def speed(dspeed):
        """Change simulation speed."""
        def func(env, _gui):
            """Wrap speed applying."""
            env.apply_speed(dspeed)
        return func

    @staticmethod
    def toggle_pause(env, _gui):
        """Pause/unpause simulation."""
        env.toggle_pause()

    @staticmethod
    def toggle_sysinfo(_env, gui):
        """Turn system info panel on/off."""
        gui.sysinfo.toggle()


class MoireBridge:
    """Class incapsulating the actions for Moire UI."""

    key_actions = {
        "[": Bridge.speed(-1),
        "]": Bridge.speed(1),
        "spacebar": Bridge.toggle_pause,
        "f12": Bridge.toggle_sysinfo,
        "escape": Bridge.exit_app,
    }


def main():
    """Run the whole environment with Moire."""
    environment = NoiseTV()
    gui = moire.GUI(runnable=environment)
    gui.run()


if __name__ == "__main__":
    main()
