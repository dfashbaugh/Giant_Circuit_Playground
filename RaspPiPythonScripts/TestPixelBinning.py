from PIL import Image
from PIL import ImageDraw

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)
draw.line( (0,0,31,31), fill=(255,0,0) )
draw.line( (0, 31, 31, 0), fill=(255,0,0) )
image.show()

px = image.load()

#Bin 16 -> 1
neoImage = Image.new("RGB", (8,8))
neoPix = neoImage.load()
for x in range(0, 8) :
	for y in range(0, 8) :
		channel1 = 0
		channel2 = 0
		channel3 = 0
		for subX in range(0,4) :
			for subY in range(0, 4) :
				theColor = px[4*x+subX, 4*y+subY]
				channel1 = channel1 + theColor[0]
				channel2 = channel2 + theColor[1]
				channel3 = channel3 + theColor[2]
		channel1 = channel1/16
		channel2 = channel2/16
		channel3 = channel3/16
		neoPix[x,y] = (channel1, channel2, channel3)

neoImage.show()