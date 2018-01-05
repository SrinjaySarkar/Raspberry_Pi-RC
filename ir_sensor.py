#interfacing of the IR proximity sensor
import RPi.GPIO as GPIO
import time
ir_sensor1=3
ir_sensor2=16
GPIO.setwarnings(False) #disabling warning messages
GPIO.setmode(GPIO.BOARD) #setting up the board for GPIO library
GPIO.setup(3,GPIO.IN)#setting pin 5 a input pin
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)#setting pin 16 as input pin
while True:
    i=GPIO.input(ir_sensor1) #accepting input of ir sensor
    j=GPIO.input(ir_sensor2) #accepting input of ir sensor
    if i==0: #checking for obstacle on left ir sensor
        print"obstacle on left",i
        time.sleep(1) #delay 
    elif j==0:
        print"Obstacle on right",j #checking for obstacle on right ir sensor
        time.sleep(1)#delay
