import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


pins = [19, 6, 13]

#enable is 19

for x in pins:
    GPIO.setup(x, GPIO.OUT)


test = input("press enter when ready")

#time.sleep(5)

GPIO.output(6, True)
GPIO.output(13, False)

GPIO.output(19, True)

time.sleep(3)

GPIO.output(19, False)
GPIO.cleanup()