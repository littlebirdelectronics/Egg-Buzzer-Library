import sys
import RPi.GPIO as GPIO

class Buzzer:
    def __init__(self, pin):
        self.__pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__pin,GPIO.OUT)
    
    def Start(self, frequency, dutyCycle=50):
        self.__buz = GPIO.PWM(self.__pin, frequency)
        self.__buz.start(dutyCycle)

    def ChangeFrequency(self, frequency):
        self.__buz.ChangeFrequency(frequency)
    
    def Stop(self):
        self.__buz.stop()
        GPIO.cleanup()