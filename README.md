A-B-C Pi
========

A simple A-B-C game for my daughters. 

I let them color pages with letters, record themselves saying the letters, and
then the app listens to key strokes and shows/plays the letter for them on the
TV through the rPi.


Requirements
------------

* SDL
* pygame


OS-X installation
-----------------

Run:

    brew tap homebrew/headonly
    brew install sdl sdl_image sdl_mixer sdl_ttf smpeg portmidi

    virtualenv --promprt=[ABC]\  .virtualenv
    source .virtualenv/bin/activate

    pip install hg+http://bitbucket.org/pygame/pygame



