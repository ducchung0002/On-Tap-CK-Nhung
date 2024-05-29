# press button to toggle led
import RPi.GPIO as GPIO
import time

# variables
BUTTON_PIN = 2
LED_PIN = 3
led_state = 0

# callback
def toggle_led(channel):
    global led_state
    led_state = 1 if led_state == 0 else 0
    GPIO.output(LED_PIN, led_state)

# set up
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=toggle_led, bouncetime=200)

GPIO.output(LED_PIN, led_state)

# loop
while True:
    time.sleep(0.01)
