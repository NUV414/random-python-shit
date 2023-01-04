from PIL import Image
import math, random

im = Image.new("HSV", (1000,1000), (255,255,255))
a1 = random.randint(-50,50)
b1 = random.randint(1,200)
c1 = random.randint(-5,5)
a2 = random.randint(-25,25)
b2 = random.randint(1,100)
c2 = random.randint(-5,5)
a3 = random.randint(-13,13)
b3 = random.randint(1,50)
c3 = random.randint(-5,5)
a4 = random.randint(-6,6)
b4 = random.randint(1,25)
c4 = random.randint(-5,5)
a5 = random.randint(-10,10)

for x in range(im.width):
	y1 = a1 * math.sin(x/b1 +c1) 
	y1 += a2 * math.cos(x/b2 + c2) 
	y1 += a3* math.sin(x/b3 + c3)
	y1 += a4 * math.cos(x/b4 +c4)
	y1 += a5 * math.sin(math.pi * x /2000) 
	for y in range(im.height):    
		if y1 >= im.height:
			im.putpixel((x,int(y1-im.height/4)), (0,0,0))
		elif x*x + y*y < 20000:
			im.putpixel((x,y), (47,190,252))
		elif (y-im.height/2) <= (y1):
			im.putpixel((x,y), (136,255,226))
		elif (y-im.height/2) > y1:
			im.putpixel((x,y), (91,255,154))
		else:
			break
print('''
a1 = {0}, b1 = {1}, c1 = {2} \n 
a2 = {3}, b2 = {4}, c2 = {5} \n 
a3 = {6}, b3 = {7}, c3 = {8}\n
a4 = {9}, b4 = {10}, c4 = {11} \n
a5 = {12}'''.format(a1, b1, c1, a2, b2, c2, a3, b3, c3, a4, b4, c4, a5))

im.show()