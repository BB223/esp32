from machine import Pin
from time import sleep
import dht

dht11 = dht.DHT11(Pin(33, Pin.IN))

while True:
    dht11.measure()
    sleep(2)
    temperature = dht11.temperature()
    humidity = dht11.humidity()

    print("Temp:\t" + str(temperature) + "C")
    print("Hum:\t" + str(humidity) + "%")
