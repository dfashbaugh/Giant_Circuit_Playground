import time
import serial
from NeoPixelMatrix import NeoPixelMatrix
from CircuitPlayGround import CircuitPlayGround
from PIL import Image
from PIL import ImageDraw

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, 31, 31), fill=(0, 100, 0), outline=(0,0,255))
draw.line( (0,0,31,31), fill=(255,0,0) )
draw.line( (0, 31, 31, 0), fill=(255,0,0) )

lastDrawTime = 0

circuitPlayground = CircuitPlayGround('/dev/cu.usbmodem1411')
neoMatrix = NeoPixelMatrix('/dev/cu.usbmodem2115241')

neoMatrix.Clear()
neoMatrix.SetImage(image, 0, 0)

while 1:
	if time.time() - lastDrawTime > 0.03 :
		neoMatrix.DrawLEDMemory()
		lastDrawTime = time.time()

	circuitPlayground.Read()
	#neoMatrix.SetAllRed(circuitPlayground.Cap12/10)