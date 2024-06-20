from machine import Pin

led = Pin(27, Pin.OUT)
led.off()

button = Pin(34, Pin.IN)

while True:
    while button.value():
        led.on()
    led.off()
