Creating audio files in OS-X
============================

There are probably better ways, but what I do is:

* Record the clip using Quick-Time. Trim it only sound the letter, and save to
  `*.m4a` files

* Convert to mp3 using:

    ffmpeg -i a.m4a a.wav
