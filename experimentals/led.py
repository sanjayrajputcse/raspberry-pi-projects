from gpiozero import LED
import time

led = LED(18)
n = input("n = ")
s = input("sleep time(in secs) = ")
while(n > 0):
    led.toggle()
    time.sleep(s)
    led.toggle()
    time.sleep(s)
    n = n - 1
