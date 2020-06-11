import time
import RPi.GPIO as GPIO
import utility
from random import randrange

delay = .5
delayDrop = 0.15

def rain_pattern(layers, cols):
    for k in range(0, 20):
        dropCount = randrange(1, 16, 1)
        drops = []
        for i in range(0, dropCount):
            col = randrange(0, 16, 1)
            drops.append(col)
        print drops
        for drop in drops:
            GPIO.output(cols[drop], GPIO.LOW)
        for j in range(0, 4):
            GPIO.output(layers[3 - j], GPIO.HIGH)
            time.sleep(delayDrop)
            GPIO.output(layers[3 - j], GPIO.LOW)
        utility.reset2(layers, cols)