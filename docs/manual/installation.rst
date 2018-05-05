Installation Instructions
=========================

**Moire** is built upon `Kivy`_ framework, it is the main dependency
for its core functionality. Also, you need `NumPy`_ in order to run
examples and tests.

.. note::
   This page currently containing instructions only for Debian-like
   systems. If you are on other system, you still can use links to
   pre-requisites in order to install them. If so, please contact us
   by `opening an issue`_ on GitHub. We could help you if you'll meet
   some troubles during installation, and also your experience could
   be used to improve this document.

Prerequisites
-------------

- `Python 3.5+`_

  Your distribution should already have all you need::

    $ sudo apt-get install python3 python3-dev python3-pip wheel

- `Kivy`_

Its pre-requisites could be installed by::

  $ sudo apt-get install \
    build-essential \
    git \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev

Then, to install stable Kivy::

  $ pip3 install Cython==0.25 Kivy==1.10.0

On latest Debian distributions you can meet conflicts with
``libsdl-mixer``. Then, try to install latest developer version,
like::

  $ pip3 install Cython==0.27.3 git\+https://github.com/kivy/kivy.git

Main package
------------

Moire package could be installed with::

  $ pip3 install moire

Note, it does not depends on pre-requisites described above, but you
still need to install them properly, or Moire will not run.

Run Moire examples
------------------

In order to run Noise TV environment with Moire::

  $ pip3 install numpy
  $ pip3 install moire
  $ wget https://raw.githubusercontent.com/a5kin/moire/master/examples/noisetv.py
  $ python3 game_of_life.py

Run tests
---------

In order to run Moire tests::

  $ git clone https://github.com/a5kin/moire.git
  $ cd moire/tests
  $ ./run_tests.sh

.. _Python 3.5+: https://www.python.org/downloads/
.. _NumPy: https://docs.scipy.org/doc/
.. _Kivy: https://kivy.org/docs/installation/installation.html
.. _Moire: https://github.com/a5kin/moire
.. _opening an issue: https://github.com/a5kin/moire/issues/new
