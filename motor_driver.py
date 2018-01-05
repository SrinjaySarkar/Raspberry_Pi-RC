#interfacing the L293D motor driver
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)#setting up GPIO library for the board
GPIO.setwarnings(False) #disabling warnings of gpio pins
GPIO.setup(7,GPIO.OUT)  #setting up pin 7 as output pin
GPIO.setup(11,GPIO.OUT) #setting up pin 11 as output pin
GPIO.setup(13,GPIO.OUT) #setting up pin 13 as output pin
GPIO.setup(5,GPIO.OUT) #setting pin 5 as output pin
#GPIO.setwarnings(False)
GPIO.setup(3,GPIO.IN)#setting pin 3 a input pin
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)#setting pin 16 as input pin
ir_sensor1=3 #assigning variables on ir sensors
ir_sensor2=16



while True:
    i=GPIO.input(ir_sensor1)
    j=GPIO.input(ir_sensor2)
    if i==0:
        time.sleep(1)
        print"going forward" #rotating the motors in clockwise direction
        GPIO.output(5,1)
        GPIO.output(7,0)
        GPIO.output(11,1)
        GPIO.output(13,0)
        #time.sleep(1)
    

    elif i==1:
        print"going backward" #rotating the motors in anticlockwise direction
        GPIO.output(5,0)
        GPIO.output(7,1)
        GPIO.output(11,0)
        GPIO.output(13,1)
        #time.sleep(1)
            

    
        

        

        
    
    
