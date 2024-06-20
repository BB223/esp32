from machine import Pin, SoftI2C
import ssd1306

scl_pin = 25
sda_pin = 26

i2c = SoftI2C(scl = Pin(scl_pin), sda = Pin(sda_pin))

display_width = 128
display_height = 64

oled = ssd1306.SSD1306_I2C(display_width, display_height, i2c)

oled.fill(0)
oled.text("Hello I2C world!", 0, 0)
oled.show()
