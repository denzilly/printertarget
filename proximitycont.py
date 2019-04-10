import RPi.GPIO as GPIO
import time
import numpy as np
import random


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

    return dist


def measure(ECHO,TRIG):

var = 1
varmax = .2223
    while (var > varmax):
        measurements = []
        # Measure 3 times
        for x in range(3):
            d = dist(ECHO,TRIG)
            time.sleep(.001)
            measurements.append(d)
        var = np.var(measurements)
        print("Distance measurement variance is: " + var)

    #if variance is acceptable, calc average distance
    pos = np.average(measurements)


xmin = #Something
xmax = #Something

    #case 1, position not violating min or max
    if (xmin < pos < xmax):

        #choose direction randomly
        if ((random() > 0.5) == True):
            dir = 'f'
            maxmove = xmax - pos
        else:
            dir = 'b'
            maxmove = pos - xmin

    #case 2, position too close to max
    if (pos > xmax):

        #Direction must be backwards
        dir = 'b'
        maxmove = pos - xmin

    #case 3, position too close to min
    if (pos > xmax):

        #Direction must be forwards
        dir = 'f'
        maxmove = xmax - pos


    #choose move Distance in mm
    dist = (random.randint(50 , maxmove))

    return dir,dist
