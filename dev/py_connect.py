import serial
import glob

def scan():
   """scan for available ports. return a list of device names."""
   return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')


port = scan()[0]
print port

ser = serial.Serial(port, 9600)

ser.write(b'1')
print "Wrote..."

