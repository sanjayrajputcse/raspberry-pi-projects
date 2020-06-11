import time
import RPi.GPIO as GPIO

delay = 0.1


def single_led_pattern(rows, cols):
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
