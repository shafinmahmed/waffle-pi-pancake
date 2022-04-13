import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)  


def contact_sensor():
    while True:
        input = GPIO.input(13)
        if (input == False):                    
                print("false")
        if (input == True):
                print("true")   
        sleep(1)


if __name__ == '__main__':
    try:
        contact_sensor()
    except KeyboardInterrupt:      #may want to change to rospy.ROSInterruptException:
        pass