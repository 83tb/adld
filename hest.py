import pyduino
a = pyduino.Arduino("/dev/tty.usbmodemfd1311")

a.digital[9].set_mode(pyduino.DIGITAL_INPUT)
#a.digital[9].set_mode(pyduino.ANALOG_INPUT)


while True:
 #a.digital[9].write(1)
 print a.digital[9].read()
 
 from time import sleep
 sleep(1)
 
 