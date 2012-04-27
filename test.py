from firmata import * 

print "Initation:"
print ""
a = Arduino('/dev/tty.usbmodemfd1311')
print "Setting the mode to OUTPUT"
a.pin_mode(9, firmata.OUTPUT)

a.delay(2)
print "Main loop."


while True:
    a.digital_write(9, firmata.HIGH)
    a.delay(2)
    print "TEst"
    a.digital_write(9, firmata.LOW)
    a.delay(2)
