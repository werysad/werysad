# tx = gpio
# vcc = pin2
# gnd = pin 6
#(disable login shell over serial, enable serial hardware)
#sudo raspi-config  - # for configuring interface I2C
#reboot
#sudo apt-get update
#sudo apt-get upgrade
#pip3 install pyserial


import serial

ser = serial.Serial('/dev/serial0', 9600, timeout=1)

print("Scan your card.....")

while True:
    data = ser.read(12)
    if data:
        print(data.decode('utf-8').strip())

#400034E6E97B
