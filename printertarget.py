import RPi.GPIO as GPIO
import time
import pygame
from threading import Thread
import numpy as np

# Initialise Pi IO Pins
GPIO.setmode(GPIO.BCM)


#move the target around
def movement():

    setup_move()


    dir = params[0]
    #####################################################insert var here
    time = params[1]/vel



    movecount=0
    while movecount<10:
        move(dir,time)
        time.sleep(0.1)
        move(b,0.35)
        movecount += 1









################################### CONTROLS HIT-RECOGNITION, LIGHTS, AND SOUND#######################################
def play():

    pygame.init()
    pygame.mixer.init()
    hitsound = pygame.mixer.Sound('ding2.wav')
    winsound = pygame.mixer.Sound('rocky.wav')


    wts = .05
    count = 1


    #Button pin
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    button_state = GPIO.input(12)
    #LED Pins
    lights = [21, 20, 16]
    for x in lights:
        GPIO.setup(x, GPIO.OUT)

    while True:

        #if button gets pressed, do this
        if button_state == False:
            #turn on one additional LED
            for x in range(count):
                GPIO.output(lights[x],True)
            #Hit sound
            hitsound.play()
            time.sleep(0.2)
            print ("Score is: " + str(count))
            count += 1

        if count == 4:
            print("you win")
            winsound.play()
            #celebratory LED display
            while count <= 30:

                for x in lights:
                    GPIO.output(x, True)
                    time.sleep(wts)
                for x in lights:
                    GPIO.output(x, False)
                    time.sleep(wts)
                count += 1

            GPIO.cleanup()

            break



############################################ PROXIMITY SENSOR MEASUREMENT TO DETERMINE MOVEMENT DISTANCES#########################################

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



def measure():

ECHO = #Something
TRIG = #Something

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



###################################################### MOVEMENT FUNCTION########################3
def move(dir, time):

    in1 = 24
    in2 = 23

    if dir == "f":

        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        print("forward")
        time.sleep(time)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)

    if dir =="b":

        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        print("backward")
        time.sleep(time)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)


def setup_move():
    in1 = 24
    in2 = 23
    en = 25
    temp1=1

    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)

    GPIO.setup(en,GPIO.OUT)

    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    p=GPIO.PWM(en,1000)
    p.start(85)

    ECHO = #set pin number
    TRIG = #set pin number
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(TRIG, GPIO.OUT)

    



if __name__ == '__main__':
    Thread(target = movement).start()
    Thread(target = play).start()
