import time

from RPi import GPIO
from RPi.GPIO import PWM

# L928 Driver
left_motors_pin1 = 8    # 3   N1 -> Grey
left_motors_pin2 = 10   # 5   N2 - purple
right_motors_pin1 = 12  # 7   N3 - Blue
right_motors_pin2 = 16  # 10   N4 - White
# +5v -> 2(Grey)
# +Gnd -> 6(Blue)

# Ultrasonic Distance Sensor
ultrasonic_distance_trig = 24   # 38     # Trig
ultrasonic_distance_echo = 22   # 40     # Echo

SAMPLE_COUNT = 1
FACTOR = 1
FULL_SPEED_DISTANCE = 200
MIN_DUTY_CYCLE = 100
MAX_DUTY_CYCLE = 100
OBSTACLE_DISTANCE = 25

delay = input('delay : ')
left_motor_pin1_pwm = None
left_motor_pin2_pwm = None
right_motor_pin1_pwm = None
right_motor_pin2_pwm = None
left_motor_pwm_duty_cycle = 0
right_motor_pwm_duty_cycle = 0


def setup_motors():
    global left_motor_pin1_pwm, right_motor_pin1_pwm, left_motor_pin2_pwm, right_motor_pin2_pwm
    global right_motor_pwm_duty_cycle, left_motor_pwm_duty_cycle

    GPIO.setup(left_motors_pin1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(left_motors_pin2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(right_motors_pin1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(right_motors_pin2, GPIO.OUT, initial=GPIO.LOW)

    left_motor_pin1_pwm = GPIO.PWM(left_motors_pin1, 50)
    left_motor_pin2_pwm = GPIO.PWM(left_motors_pin2, 50)
    right_motor_pin1_pwm = GPIO.PWM(right_motors_pin1, 50)
    right_motor_pin2_pwm = GPIO.PWM(right_motors_pin2, 50)

    left_motor_pin1_pwm.start(0)
    left_motor_pin2_pwm.start(0)
    right_motor_pin1_pwm.start(0)
    right_motor_pin2_pwm.start(0)


def setup_distance_sensor():
    GPIO.setup(ultrasonic_distance_trig, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ultrasonic_distance_echo, GPIO.IN)


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # L298
    setup_motors()

    # Distance Sensor
    setup_distance_sensor()


def get_distance():
    GPIO.output(ultrasonic_distance_trig, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(ultrasonic_distance_trig, GPIO.LOW)
    while not GPIO.input(ultrasonic_distance_echo):
        pass
    t1 = time.time()
    while GPIO.input(ultrasonic_distance_echo):
        pass
    t2 = time.time()
    return (t2-t1) * 340 / 2 * 100


def get_avg_distance():
    counter = SAMPLE_COUNT
    total_distance = 0
    while counter > 0:
        total_distance += get_distance()
        # time.sleep(0.05)
        counter -= 1
    return total_distance / SAMPLE_COUNT


def reset_motors():
    left_motor_pin1_pwm.ChangeDutyCycle(0)
    left_motor_pin2_pwm.ChangeDutyCycle(0)
    right_motor_pin1_pwm.ChangeDutyCycle(0)
    right_motor_pin2_pwm.ChangeDutyCycle(0)


def left_wheels_forward():
    print "DEBUG: left motors forward duty cycle : " + str(left_motor_pwm_duty_cycle)
    left_motor_pin1_pwm.ChangeDutyCycle(left_motor_pwm_duty_cycle)


def left_wheels_reverse():
    print "DEBUG: left motors reverse duty cycle : " + str(left_motor_pwm_duty_cycle)
    left_motor_pin2_pwm.ChangeDutyCycle(left_motor_pwm_duty_cycle)


def right_wheels_forward():
    print "DEBUG: right motors forward duty cycle : " + str(right_motor_pwm_duty_cycle)
    right_motor_pin1_pwm.ChangeDutyCycle(right_motor_pwm_duty_cycle)


def right_wheels_reverse():
    print "DEBUG: right motors reverse duty cycle : " + str(right_motor_pwm_duty_cycle)
    right_motor_pin2_pwm.ChangeDutyCycle(right_motor_pwm_duty_cycle)


def move_forward():
    print "moving forward"
    left_wheels_forward()
    right_wheels_forward()


def move_reverse():
    left_wheels_reverse()
    right_wheels_reverse()


def move_left():
    print "obstacle found, moving left"
    left_wheels_reverse()
    right_wheels_forward()


def move_right():
    print "obstacle found, moving right"
    left_wheels_forward()
    right_wheels_reverse()


def loop():
    global left_motor_pwm_duty_cycle, right_motor_pwm_duty_cycle
    while True:
        original_distance = round(get_avg_distance(), 2)
        distance = original_distance
        print str(distance) + " cms"
        if distance > FULL_SPEED_DISTANCE:
            distance = FULL_SPEED_DISTANCE
        target_duty_cycle = round(distance / 2, 2)
        if target_duty_cycle < MIN_DUTY_CYCLE:
            target_duty_cycle = MIN_DUTY_CYCLE
        if target_duty_cycle > MAX_DUTY_CYCLE:
            target_duty_cycle = MAX_DUTY_CYCLE
        left_motor_pwm_duty_cycle += round((target_duty_cycle - left_motor_pwm_duty_cycle) * FACTOR, 2)
        right_motor_pwm_duty_cycle += round((target_duty_cycle - right_motor_pwm_duty_cycle) * FACTOR, 2)
        if original_distance > OBSTACLE_DISTANCE:
            reset_motors()
            move_forward()
        else:
            reset_motors()
            move_reverse()
            time.sleep(1)
            reset_motors()
            move_right()
            time.sleep(2)
        time.sleep(delay)


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        loop()
        destroy()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
exit(0)

