"""
The official GUI for `Artipixoids!`_ project.

It is integrating natively with `Xentica`_ framework, but you may also
use it to visualize your own step-by-step simulations.

The engine is dealing nothing with rendering, it's relying fully on
frames rendered with your simulation. So, you should manually
implement the stuff like zooming or scrolling, and bind the actions to
keyboard/mouse/etc events.

The only thing Moire doing right now, is keeping the rate of your
rendered frames, speeding simulation up/down as necessary. Also,
system info dialog is included, showing current timestep, frames/steps
per second and simulation speed.

.. _Artipixoids!: http://artipixoids.a5kin.net/concept/artipixoids_concept.pdf
.. _Xentica: https://github.com/a5kin/xentica/

"""

from moire.main import GUI


__all__ = [
    'GUI',
]
