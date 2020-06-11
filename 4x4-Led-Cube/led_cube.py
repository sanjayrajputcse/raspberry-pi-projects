import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

delay = 0.05
delayLayer = 0.2

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


rows = [3, 5, 7, 8]
cols = [10, 12, 11, 13, 15, 16, 18, 19, 21, 23, 22, 24, 26, 31, 33, 35]



def single_led_pattern():
    for row in rows:
        print("Layer : " + str(row))
        GPIO.output(row, GPIO.HIGH)
        for col in cols:
            print("LED ON : " + str(col))
            GPIO.output(col, GPIO.LOW)
            time.sleep(delay)
            print("LED OFF : " + str(col))
            GPIO.output(col, GPIO.HIGH)
        GPIO.output(row, GPIO.LOW)



def layer_pattern():
    #Front Top
    for col in cols:
        GPIO.output(col, GPIO.LOW)
    for i in range(0, 4):
        GPIO.output(rows[3 - i], GPIO.HIGH)
        time.sleep(delayLayer)
        GPIO.output(rows[3 - i], GPIO.LOW)
    for col in cols:
        GPIO.output(col, GPIO.HIGH)
    #From Front
    for row in rows:
        GPIO.output(row, GPIO.HIGH)
    for i in range(0, 4):
        print("Layer(From Front) " + str(i + 1))
        for start in range(i * 4, i * 4 + 4):
            GPIO.output(cols[start], GPIO.LOW)
        time.sleep(delayLayer)
        for start in range(i * 4, i * 4 + 4):
            GPIO.output(cols[start], GPIO.HIGH)
    #From Left
    for i in range(0, 4):
        print("Layer(From Left) " + str(i + 1))
        start = i
        for j in range(0, 4):
            GPIO.output(cols[start], GPIO.LOW)
            start = start + 4
        time.sleep(delayLayer)
        start = i
        for j in range(0, 4):
            GPIO.output(cols[start], GPIO.HIGH)
            start = start + 4
    for row in rows:
        GPIO.output(row, GPIO.LOW)


try:
    
    for pin in rows:
        print("Setup Pin : " + str(pin))
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    for pin in cols:
        print("Setup Pin : " + str(pin))
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
    time.sleep(2)
    while True:
 
        #Single LED PATTERN
        single_led_pattern()  
        time.sleep(0.1)

        #Layer wise Patter
        layer_pattern()
        time.sleep(delayLayer)
        layer_pattern()
        time.sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit

