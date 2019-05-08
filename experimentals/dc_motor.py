import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

enableAPin1=8
enableAPin2=10
motorAPin1=16
motorAPin2=18

delay = input('delay : ')

GPIO.setup(enableAPin1, GPIO.OUT)
GPIO.setup(enableAPin2, GPIO.OUT)

GPIO.setup(motorAPin1, GPIO.OUT)
GPIO.setup(motorAPin2, GPIO.OUT)

GPIO.output(enableAPin1, GPIO.HIGH)
GPIO.output(enableAPin2, GPIO.HIGH)

p = GPIO.PWM(motorAPin1,50)
q = GPIO.PWM(motorAPin2, 50)
p.start(0)
q.start(0)
try:
    while True:
        for i in range(100):
            p.ChangeDutyCycle(i)
            time.sleep(delay)
        for i in range(100):
            p.ChangeDutyCycle(100-i)
            time.sleep(delay)
        
        p.ChangeDutyCycle(0)
        
        for i in range(100):
            q.ChangeDutyCycle(i)
            time.sleep(delay)
        for i in range(100):
            q.ChangeDutyCycle(100-i)
            time.sleep(delay)
        
        q.ChangeDutyCycle(0)
except KeyboardInterrupt:
    p.stop
    q.stop
#GPIO.output(motorAPin1, GPIO.LOW)
#GPIO.output(motorAPin2, GPIO.HIGH)
#time.sleep(delay)
#GPIO.output(motorAPin1, GPIO.HIGH)
#GPIO.output(motorAPin2, GPIO.LOW)
#time.sleep(delay)

GPIO.cleanup()
exit



