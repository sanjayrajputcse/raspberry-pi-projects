from RPi import GPIO
import time
from gpiozero import LED

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
exit(0)