import machine
import time

pin = machine.Pin(25, machine.Pin.OUT)

def toggle(p):
    p.value(not p.value())

while True:
    toggle(pin)
    time.sleep(1)

