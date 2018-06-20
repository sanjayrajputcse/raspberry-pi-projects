from RPi import GPIO
import time
import requests
import sys

sys.stdout = open('/var/log/moksha/plant-watering-system/app.log', 'w')

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

APP_ID = "plant-watering-system"
ActionURL = "http://35.231.5.148:20000/v0/applications/actions"
RelayPin = 12    # pin11

def setup():
    GPIO.setmode(GPIO.BOARD)         # Numbers pins by physical location
    GPIO.setup(RelayPin, GPIO.OUT)   # Set pin mode as output
    GPIO.output(RelayPin, GPIO.LOW)

def loop():
    while True:
        headers = {"APP_ID": APP_ID}
        print("making call to google cloud machine to get new actions")
        response = requests.get(url=ActionURL, headers=headers)
        data = response.json()
        print(response.status_code)
        print(data)
        if response.status_code == 200 and len(data) > 0:
            setup()
            print("activating timer for " + data[0]['time'] + " " + data[0]['timeUnit'])
            action_id = data[0]['id']
            sleep_time = data[0]['time']
            print("calling update action api call: start action")
            requests.put(url=ActionURL + "/" + str(action_id) + "/start", headers=headers)
            GPIO.output(RelayPin, GPIO.HIGH)
            time.sleep(float(sleep_time))
            GPIO.output(RelayPin, GPIO.LOW)
            destroy()
            print("calling update action api call: end action")
            requests.put(url=ActionURL + "/" + str(action_id) + "/end", headers=headers)
        time.sleep(1)

def destroy():
    GPIO.output(RelayPin, GPIO.LOW)
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    # setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
exit(0)
