import os
import serial
import urllib

CURRENTDIR = os.path.dirname(__file__)
BASEDIR = os.path.dirname(CURRENTDIR)
SER = serial.Serial('COM3', 9600)
h = 0
v = 0

class HeadSetCore():
	"""docstring for HeadSetCore"""
	def index(self, req):
		global h
		global v
		r = str(urllib.unquote_plus(req)).split(":")
		if r[0] == "H" or r[0] == "h":
			h += int(r[1])
			if h < 0:
				h = 0
			if h > 180:
				h = 180
			req = "H:%i" % h
		if r[0] == "V" or r[0] == "v":
			v += int(r[1])
			if v < 0:
				v = 0
			if v > 180:
				v = 180
			req = "V:%i" % v
		if r[0] == "L" or r[0] == "l":
			req = "L:%i" % int(r[1])
		if r[0] == "C" or r[0] == "c":
			req = "C"
		print req
		SER.write(req)

if __name__ == "__main__":
    print "Hello World";