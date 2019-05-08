import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

delay = input('delay: ')
GPIO.setup(7, GPIO.OUT)

pulse = GPIO.PWM(7,50)
pulse.start(7.5)


try:
    while True:
        pulse.ChangeDutyCycle(7.5)
        time.sleep(delay)
        pulse.ChangeDutyCycle(12.5)
        time.sleep(delay)
        pulse.ChangeDutyCycle(7.5)
        time.sleep(delay)
        pulse.ChangeDutyCycle(2.5)
        time.sleep(delay)

except KeyboardInterrupt:
    pulse.stop
    GPIO.cleanup()
    exit

