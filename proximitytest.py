import RPi.GPIO as GPIO
import time


ECHO = #set pin number
TRIG = #set pin number
GPIO.setmode(GPIO.BCM)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG, GPIO.OUT)


def dist(ECHO,TRIG):

    #activate board
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    #measure distance
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_dur = pulse_end - pulse_start

    #speed of sound/2 * time taken
    dist = 171500 * pulse_dur

    print('dist')
