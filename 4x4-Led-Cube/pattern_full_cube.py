from time import sleep
import RPi.GPIO as GPIO
import utility

delay = 1


def full_cube(layers, grid):
    for i in range(0, 3):
        utility.on_all_layers(layers)
        utility.on_all_grid(grid)
        sleep(delay)
        utility.reset(layers, grid)
        sleep(0.5)
