from time import sleep
import RPi.GPIO as GPIO
import utility

delay = 0.2


def cube_4x4(layers, grid):
    utility.on_all_layers(layers)
    GPIO.output(grid[0][0], GPIO.LOW)
    GPIO.output(grid[0][3], GPIO.LOW)
    GPIO.output(grid[3][0], GPIO.LOW)
    GPIO.output(grid[3][3], GPIO.LOW)
    sleep(delay)
    utility.reset(layers, grid)


def cube_2x2(layers, grid):
    GPIO.output(layers[1], GPIO.HIGH)
    GPIO.output(layers[2], GPIO.HIGH)
    for i in range(1, 3):
        for j in range(1, 3):
            GPIO.output(grid[i][j], GPIO.LOW)
    sleep(delay)
    utility.reset(layers, grid)


def cube_pattern(layers, grid):
    for i in range(0, 4):
        cube_4x4(layers, grid)
        cube_2x2(layers, grid)
