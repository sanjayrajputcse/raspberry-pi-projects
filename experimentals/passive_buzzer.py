import time
import RPi.GPIO as GPIO

# S8050, 1K, Green Base Buzzer

BZRPin = 7
delay = input('Delay: ')
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BZRPin, GPIO.OUT)
GPIO.output(BZRPin, GPIO.LOW)
p = GPIO.PWM(BZRPin, 50) #50GHZ
p.start(50) #Duty Cycle 50%
try:
    while True:
        for freq in range(100, 2000, 100):
            p.ChangeFrequency(freq)
            time.sleep(delay)
        for freq in range(2000, 100, -100):
            p.ChangeFrequency(freq)
            time.sleep(delay)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
    exit

