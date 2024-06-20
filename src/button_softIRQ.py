from machine import Pin
from time import sleep
import micropython

led = Pin(27, Pin.OUT)
led.off()

def handle_interrupt(pin):
    micropython.schedule(flash_led, None)

def flash_led(foo):
    global led
    led.on()
    sleep(1)
    led.off()

button = Pin(34, Pin.IN)
button.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
    sleep(0.25)
