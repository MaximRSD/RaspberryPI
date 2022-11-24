import RPi.GPIO as GPIO
import time

LED_PIN = 20
BUTTON_PIN = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)

# while True:
#     GPIO.output(LED_PIN, GPIO.HIGH)

while True:
    buttonState = GPIO.input(BUTTON_PIN)

    if buttonState == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
