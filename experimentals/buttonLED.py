from RPi import GPIO
import time

LedPin = 7;
BtnPin = 11;

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(LedPin, GPIO.LOW)

try:
    while True:
        if GPIO.input(BtnPin) == GPIO.LOW:
            print 'led...on'
            GPIO.output(LedPin, GPIO.HIGH)
        else:
            print 'led..off'
            GPIO.output(LedPin, GPIO.LOW)
        time.sleep(.1)
except KeyboardInterrupt:
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()
    exit

