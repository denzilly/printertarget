import RPi.GPIO as GPIO
import time
import pygame
from threading import Thread

# Initialise Pi IO Pins
GPIO.setmode(GPIO.BCM)


#move the target around
def move():


    in1 = 24
    in2 = 23
    en = 25
    temp1=1


    movecount=0
    while movecount<10:
        GPIO.setup(in1,GPIO.OUT)
        GPIO.setup(in2,GPIO.OUT)

        GPIO.setup(en,GPIO.OUT)

        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        p=GPIO.PWM(en,1000)
        p.start(85)

        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        print("forward")
        time.sleep(0.35)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        time.sleep(0.35)
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        movecount += 1



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


if __name__ == '__main__':
    Thread(target = move).start()
    Thread(target = play).start()
