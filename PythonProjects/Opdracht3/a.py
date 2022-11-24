import RPi.GPIO as GPIO
import time

LED_PIN = 16
LED_PIN1 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN1, GPIO.OUT)

while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.output(LED_PIN1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(LED_PIN1, GPIO.LOW)
    time.sleep(1)