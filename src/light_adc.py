from machine import Pin, ADC, PWM
from time import sleep

ldr = ADC(Pin(34, Pin.IN))
ldr.atten(ADC.ATTN_11DB)

led = PWM(Pin(27, Pin.OUT))

while True:
    brightness = ldr.read()
    print(brightness)

    scaled_value = int(brightness / 4)
    led.duty(1023 - scaled_value)

    sleep(0.5)
