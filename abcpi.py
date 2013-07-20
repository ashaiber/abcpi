#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A-B-C Pi game

Listens to letter key strokes (a-z), and when relevant shows an image and play a
sound of the letter. 

If the image/sound for the letter is missing, it says so to encourage the kid to
create the art.
"""

import os
from collections import namedtuple
import pygame
from pygame.locals import K_ESCAPE, QUIT, KEYDOWN

LETTERS = 'abcdefghijklmnopqrstuvwxyz0'

Letter = namedtuple('Letter', ('image', 'sound'))


def load_media():
    letters = {}
    for letter in LETTERS:
        image_file = r'images/{0}.jpg'.format(letter)
        audio_file = r'audio/{0}.wav'.format(letter)

        if os.path.exists(image_file) and os.path.exists(audio_file):
            # Load the image and sound
            try:
                image = pygame.image.load(image_file).convert()
                sound = pygame.mixer.Sound(audio_file)

                letters[letter] = Letter(image=image, sound=sound)

                print("Found the letter '{0}'".format(letter))
            except Exception as e:
                print("Failed to load the letter '{0}'\n{1}".format(letter, e))
    return letters


def main():
    pygame.init()
    pygame.mixer.init()

    SW, SH = 1280, 720
    background_position = [0, 0]

    screen = pygame.display.set_mode((SW, SH))
    pygame.display.set_caption('A-B-C-Pi')

    letters = load_media()

    # game loop
    game_in_progress = True

    while game_in_progress:
        for e in pygame.event.get():
            if e.type is QUIT or \
               e.type is KEYDOWN and e.key == K_ESCAPE:
                game_in_progress = False

            elif e.type is KEYDOWN:
                try:
                    letter = chr(e.key).lower()
                    if letter in letters:

                        im = pygame.transform.scale(letters[letter].image, (SW, SH))
                        im.set_colorkey((255, 100, 255))

                        screen.blit(im, background_position)
                        pygame.display.flip()
                        letters[letter].sound.play()
                except:
                    pass

    pygame.mixer.quit()
    pygame.quit()

if __name__ == '__main__':
    main()
