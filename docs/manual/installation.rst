Installation Instructions
=========================

**Moire** is built upon `Kivy`_ framework, it is the main dependency
for its core functionality. Also, you need `NumPy`_ in order to run
examples and tests.

.. warning::
   This page *may* give you some insights on how to set up your
   environment and run Moire examples, but without any
   guarantees. More detailed instructions are coming soon.

Prerequisites
-------------

- `Python 3.5+`_

- `Kivy`_

Possible solution for Debian-like systems::

  $ sudo apt-get install python3
  $ sudo pip3 install Cython==0.23
  $ sudo pip3 install kivy

Run Moire examples
------------------

In order to run Noise TV environment with Moire:

1. Clone `Moire`_ repository.

2. Put it on Python path.

3. Install `NumPy`_.

4. Run ``moire/examples/noisetv.py`` with Python 3 interpreter.

Possible solution for Debian-like systems::

  $ mkdir moire
  $ cd moire
  $ git clone https://github.com/a5kin/moire.git
  $ PYTHONPATH="$(pwd)/moire/:$PYTHONPATH" python3 ./moire/examples/noisetv.py

.. _Python 3.5+: https://www.python.org/downloads/
.. _NumPy: https://docs.scipy.org/doc/
.. _Kivy: https://kivy.org/docs/installation/installation.html
.. _Moire: https://github.com/a5kin/moire
