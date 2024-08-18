import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led_red = 24
led_blue = 25
led_yellow = 23
relay_pin = 16
state=False
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_blue, GPIO.OUT)
GPIO.setup(led_yellow, GPIO.OUT)
GPIO.output(relay_pin,state)
GPIO.output(led_red,state)
GPIO.output(led_blue,state)
GPIO.output(led_yellow,state)
GPIO.cleanup()
