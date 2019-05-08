import time
import RPi.GPIO as GPIO

BeepPin = 7
delay = input('Delay: ')
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BeepPin, GPIO.OUT)
GPIO.output(BeepPin, GPIO.HIGH)
try:
    while True:
        GPIO.output(BeepPin, GPIO.LOW)
        time.sleep(delay)
        GPIO.output(BeepPin, GPIO.HIGH)
        time.sleep(delay)
except KeyboardInterrupt:
    GPIO.output(BeepPin, GPIO.HIGH)
    GPIO.cleanup()
    exit

