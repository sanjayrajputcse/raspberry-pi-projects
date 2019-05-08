import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

delay = input('delay : ')

InputPin = [7,11,13,15]

for pin in InputPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)

halfSteppingSeq = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]   ]

fullSteppingSeq = [ [1,0,0,0],
        [0,0,0,1],
        [0,0,1,0],
        [0,1,0,0]   ]

for i in range(512):
    for step in range(4):
        for pin in range(4):
            GPIO.output(InputPin[pin], fullSteppingSeq[step][pin])
        time.sleep(delay)

GPIO.cleanup()
exit
