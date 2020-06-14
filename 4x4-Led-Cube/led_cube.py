import time
import RPi.GPIO as GPIO
from pattern_layer import layer_pattern
from pattern_single_led import single_led_pattern
from pattern_cube import cube_pattern
from pattern_rain import rain_pattern
from pattern_full_cube import full_cube
from pattern_snake import snake_game

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

delay = 0.1

L1 = 3
L2 = 5
L3 = 7
L4 = 8

A1 = 10
A2 = 12
A3 = 11
A4 = 13
A5 = 15
A6 = 16
A7 = 18
A8 = 19
A9 = 21
A10 = 23
A11 = 22
A12 = 24
A13 = 26
A14 = 31
A15 = 33
A16 = 35


layers = [3, 5, 7, 8]
cols = [10, 12, 11, 13, 15, 16, 18, 19, 21, 23, 22, 24, 26, 31, 33, 35]
grid = [
        [A1, A2, A3, A4],
        [A5, A6, A7, A8],
        [A9, A10, A11, A12],
        [A13, A14, A15, A16]
       ]

try:
    
    for pin in layers:
        print("Setup Pin : " + str(pin))
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    for pin in cols:
        print("Setup Pin : " + str(pin))
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
    while True:

        # Single LED PATTERN
        single_led_pattern(layers, cols)

        # Layer wise Patter
        layer_pattern(layers, cols)

        # Cube
        cube_pattern(layers, grid)

        # Rain
        rain_pattern(layers, cols)

        # full_cube
        full_cube(layers, grid)

        # snake
        snake_game(layers, grid)


except (Exception, KeyboardInterrupt) as e:
    print(e)
    GPIO.cleanup()
    exit

