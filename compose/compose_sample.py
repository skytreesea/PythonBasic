import pygame
import time

pygame.init()

# Set up the sound system
pygame.mixer.init()

# Define the sound for each note
sounds = {}
for note in scale_notes:
    sounds[note] = pygame.mixer.Sound(note + ".wav")

# Play the melody
for note in melody:
    sounds[note].play()
    time.sleep(0.5)