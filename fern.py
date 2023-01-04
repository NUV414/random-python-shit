from PIL import Image
import random
import numpy as np

im = Image.new("RGB",(1000,1000),(255,255,255))

def f1(Point, a=0, b=0, c=0, d=0.16, e=0, f=0):
    return (a*Point[0]+b*Point[1]+e,c*Point[0] + d * Point[1]+ f)
def f2(Point, a=0.85, b=0.04, c=-0.04, d=0.85, e=0, f=1.60):
    return (a* Point[0] + b*Point[1]+e,c*Point[0] + d*Point[1]+f)
def f3(Point, a=0.2, b=-0.26, c=0.23, d=0.22, e=0, f=1.6):
    return (a*Point[0] +b*Point[1]+e,c*Point[0]+d*Point[1]+f)
def f4(Point, a=-0.15, b=0.28, c= 0.26, d=0.25, e=0, f=0.44):
    return (a*Point[0]+b*Point[1]+e,c * Point[0] + d*Point[1] + f)

step = 0
point = (0,0)
while step <= 1100000:
    functions = [f1(point), 
    f2(point),
    f3(point), 
    f4(point)]
    point2 = (int((point[0]+2.182)*im.width/(2.6558*2))%im.width, -int(point[1]*im.height/9.9983)%im.height)
    im.putpixel(point2, (0,255,0))
    point = random.choices(functions,weights= (1,85,7,7))[0]
    step += 1

im.show()