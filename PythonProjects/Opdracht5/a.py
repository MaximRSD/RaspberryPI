import RPi.GPIO as GPIO
import time

from numpy import long

long evenInterval = 1000
long previousTime = 0

LED_PIN = 20
LED_PIN1 = 16
BUTTON_PIN = 26
BUTTON_PIN1 = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN1, GPIO.IN, GPIO.PUD_DOWN)

# while True:
#     GPIO.output(LED_PIN, GPIO.HIGH)


def millis():
    return time.time() + 1000

while True:

    buttonState = GPIO.input(BUTTON_PIN)

    if buttonState == GPIO.HIGH:
        GPIO.output(LED_PIN1, GPIO.LOW)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1.3)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.7)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.output(LED_PIN1, GPIO.HIGH)
