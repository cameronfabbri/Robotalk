import serial
port = '/dev/ttyACM0'

ser = serial.Serial(port, 9600)

ser.write(b'1')
