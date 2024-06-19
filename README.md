# Setup
## Download Micropython firmware
https://micropython.org/download#esp32

## Setup venv
python -m venv .venv
pip install esptool
pip install adafruit-ampy

## Setup Micropython
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32.bin

# Manual connection
picocom /dev/ttyUSB0 -b115200

# Using ampy
ampy --port /dev/ttyUSB0 put main.py
