from machine import TouchPad, Pin, PWM
from time import sleep

RED_TOUCH = 12
GREEN_TOUCH = 14
BLUE_TOUCH = 27

RED_PIN = 32
GREEN_PIN = 33
BLUE_PIN = 25

touchR = TouchPad(Pin(RED_TOUCH, Pin.IN))
touchG = TouchPad(Pin(GREEN_TOUCH, Pin.IN))
touchB = TouchPad(Pin(BLUE_TOUCH, Pin.IN))

ledR = PWM(Pin(RED_PIN, Pin.OUT))
ledG = PWM(Pin(GREEN_PIN, Pin.OUT))
ledB = PWM(Pin(BLUE_PIN, Pin.OUT))

def setRed(on):
    ledR.duty(511) if on else ledR.duty(0)

def setGreen(on):
    ledG.duty(767) if on else ledG.duty(0)

def setBlue(on):
    ledB.duty(1023) if on else ledB.duty(0)

while True:
    tR = touchR.read() < 200
    tG = touchG.read() < 200
    tB = touchB.read() < 200

    setRed(tR)
    setGreen(tG)
    setBlue(tB)

    sleep(0.5)

