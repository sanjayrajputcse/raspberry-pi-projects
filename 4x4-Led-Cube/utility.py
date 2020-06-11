from time import sleep
import RPi.GPIO as GPIO


def reset_layers(layers):
    for layer in layers:
        GPIO.output(layer, GPIO.LOW)


def on_all_layers(layers):
    for layer in layers:
        GPIO.output(layer, GPIO.HIGH)


def reset_cols(cols):
    for col in cols:
        GPIO.output(col, GPIO.HIGH)


def on_all_cols(cols):
    for col in cols:
        GPIO.output(col, GPIO.LOW)


def reset_grid(grid):
    for row in range(0, 4):
        for col in range(0, 4):
            GPIO.output(grid[row][col], GPIO.HIGH)


def on_all_grid(grid):
    for row in range(0, 4):
        for col in range(0, 4):
            GPIO.output(grid[row][col], GPIO.LOW)


def reset(layers, grid):
    reset_layers(layers)
    reset_grid(grid)

def reset2(layers, cols):
    reset_layers(layers)
    reset_cols(cols)
