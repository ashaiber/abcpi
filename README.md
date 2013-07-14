A-B-C Pi
========

A simple A-B-C game I wrote for the Raspberry-Pi. 

It takes a folder of images (one for each letter) and a folder of audio files 
(recordings of the ABC letters), and reacts to key-strokes by showing the image 
on the TV and playing the recording.

I let my daughters color pages with letters, record themselves saying the letters, 
and they have a blast seeing the TV reacting to the key-strokes with their drawings 
and recordings.


Pre-requisites
------------

* SDL
* pygame


rPi Installation
-----------------

    git clone git@github.com:ashaiber/abcpi.git
    cd abcpi
    ./abcpi.py



OS-X installation
-----------------

Run:

    brew tap homebrew/headonly
    brew install sdl sdl_image sdl_mixer sdl_ttf smpeg portmidi

    git clone git@github.com:ashaiber/abcpi.git
    cd abcpi
    
    virtualenv --prompt=[ABC]\  .virtualenv
    source .virtualenv/bin/activate

    pip install hg+http://bitbucket.org/pygame/pygame

    ./abcpi.py

