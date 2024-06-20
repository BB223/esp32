from machine import Pin
from time import sleep

led = Pin(27, Pin.OUT)
led.off()

def handle_interrupt(pin):
    global led
    led.on()
    sleep(1)
    led.off()

button = Pin(34, Pin.IN)
button.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
    sleep(0.25)
