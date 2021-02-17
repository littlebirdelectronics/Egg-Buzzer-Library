import sys
import RPi.GPIO as GPIO

class Buzzer:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.OUT)
    
    def Freq(self, frequency, dutyCycle=25):
        self.buz = GPIO.PWM(self.pin, frequency)
        self.buz.start(dutyCycle)
    
    def Stop(self):
        self.buz.stop();