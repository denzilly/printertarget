import RPi.GPIO as GPIO
import time
from playsound import playsound

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

lights = [17, 27, 22]
wts = .05
count = 1
#pygame.mixer.init()
#pygame.mixer.music.load('blast.wav')


while True:
    button_state = GPIO.input(23)

    
    if button_state == False:
        for x in range(count):
            GPIO.output(lights[x],True)
            
        time.sleep(0.2)
        print ("Score is: " + str(count))
        count += 1
        
    if count == 4:
        print("you win")
            
        while count <= 30:
            GPIO.output(17, True)
            time.sleep(wts)
            GPIO.output(27, True)
            time.sleep(wts)
            GPIO.output(22, True)
            time.sleep(wts)
            GPIO.output(17, False)
            time.sleep(wts)
            GPIO.output(27, False)
            time.sleep(wts)
            GPIO.output(22, False)
            time.sleep(wts)
            count += 1
            
        for x in lights:
            GPIO.output(x, False)
            
        GPIO.cleanup()
        break
