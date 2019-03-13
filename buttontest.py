import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

lights = [21, 20, 16]

for x in lights:
    GPIO.setup(x, GPIO.OUT)


wts = .05
count = 1

pygame.init()
pygame.mixer.init()
hitsound = pygame.mixer.Sound('ding2.wav')
winsound = pygame.mixer.Sound('russia2.wav')


while True:
    button_state = GPIO.input(12)

    
    if button_state == False:
        for x in range(count):
            GPIO.output(lights[x],True)
        hitsound.play()   
        time.sleep(0.2)
        print ("Score is: " + str(count))
        count += 1
        
    if count == 4:
        print("you win")
        winsound.play()    
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
