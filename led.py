from gpiozero import LED
import time

l1 = LED(20)#pi pin 38
l2 = LED(21)#pi pin 40
l3 = LED(17)|#pi pin 11
l1.on()
time.sleep(1)
l1.off()
l2.on()
time.sleep(2)
l3.on()
time.sleep(5)
l2.off()
l3.off()

#Blink 1 led 
# from gpiozero import LED
# Import time 

# led=LED(17)#pi pin 11
# led.on()
# time sleep(1)
# led.off()
# time sleep(1)
# led.on()
# time sleep(1)
# led.off()
# time sleep(1)
# led.on()
# time sleep(1)
# led.off()

# Toggle 2 led 
# from gpiozero import LED
# Import time 

# led=LED(17)#pi pin 11
# led1=LED(27)#PI PIN 13
# led.on()
# time sleep(1)
# led.off()
# led1.on()
# time sleep(1)
# led.on()
# led1.off()
# time sleep(1)
# led.off()
# led1.on()
# time sleep(1)
# led.on()
# led1.off()
# time sleep(1)
# led.off()
