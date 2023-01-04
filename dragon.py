from PIL import Image
import random
import math

im = Image.new("RGB",(500,500),(0,0,0))

def f1(z):
    return 0.5*(complex(1,1)*z)
def f2(z):
    return 1-0.5*(complex(1,-1)*z)

step = 0
point = complex(0,1)
while step <= 1100000:
    functions = [f1, f2]
    point2 = (int((point.real-im.width/2)*im.width/2**0.5)%im.width, int((point.imag-im.height/2)*im.height/2**0.5)%im.height)
    im.putpixel(point2, (int(math.log(abs(point2[0]+1))),0,point2[1]))
    point = random.choices(functions,weights= (1,1))[0](point)
    step += 1

im.show()