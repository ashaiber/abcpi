Adding letter images
====================

* Draw the letter in the middle of the page. Make sure to leave some margin area.

* Save the image as 'letter.jpg' in this folder, i.e. 'a.jpg' for 'a'.

* Size the image to 1920x1080 (this assumes a rotated 2335x1650 image. Adjust for other size/orientation):

    gm mogrify -rotate -90 -resize 1920x1357 -crop 1920x1080+0+138 a.jpg



