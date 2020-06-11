import time
import RPi.GPIO as GPIO

delay = 0.1


def layer_pattern(rows, cols):

    # From Front Top to Bottom and Reverse
    for col in cols:
        GPIO.output(col, GPIO.LOW)
    for i in range(0, 4):
        GPIO.output(rows[3 - i], GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(rows[3 - i], GPIO.LOW)
    for i in range(0, 4):
        GPIO.output(rows[i], GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(rows[i], GPIO.LOW)
    for col in cols:
        GPIO.output(col, GPIO.HIGH)

    # From Front to Back and Reverse
    for row in rows:
        GPIO.output(row, GPIO.HIGH)
    for i in range(0, 4):
        print("Layer(From Front) " + str(i + 1))
        for start in range(i * 4, i * 4 + 4):
            GPIO.output(cols[start], GPIO.LOW)
        time.sleep(delay)
        for start in range(i * 4, i * 4 + 4):
            GPIO.output(cols[start], GPIO.HIGH)
    for i in range(0, 4):
        print("Layer(From Front) " + str(i + 1))
        for start in range(i * 4, i * 4 + 4):
            GPIO.output(cols[15 - start], GPIO.LOW)
        time.sleep(delay)
        for start in range(i * 4, i * 4 + 4):
            GPIO.output(cols[15 - start], GPIO.HIGH)
    for row in rows:
        GPIO.output(row, GPIO.HIGH)

    # From Left to Right and Reverse
    for i in range(0, 4):
        print("Layer(From Left) " + str(i + 1))
        start = i
        for j in range(0, 4):
            GPIO.output(cols[start], GPIO.LOW)
            start = start + 4
        time.sleep(delay)
        start = i
        for j in range(0, 4):
            GPIO.output(cols[start], GPIO.HIGH)
            start = start + 4
    for i in range(0, 4):
        print("Layer(From Left) " + str(i + 1))
        start = i
        for j in range(0, 4):
            GPIO.output(cols[15 - start], GPIO.LOW)
            start = start + 4
        time.sleep(delay)
        start = i
        for j in range(0, 4):
            GPIO.output(cols[15 - start], GPIO.HIGH)
            start = start + 4
    for row in rows:
        GPIO.output(row, GPIO.LOW)
