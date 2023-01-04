from PIL import Image
import math, time

r=2
iterations = 512
im = Image.new("RGB", (512,512), (255,255,255))
for y in range(im.height):
    for x in range(im.width):
        x1 = (1/(im.width / 4)) * (x-im.width/2) #scales the canvas to be -2 <= x <= 2
        y1 = (1/(im.height /4)) * (y-im.height/2) # scales the canvas to be -2 <= y <= 2
        c = complex(x1,y1) # gets a complex number at the point x1 y1
        z = complex(0,0) # initial value for the mandelbrot set z=0
        maxorb = 0 # colouring thing, ignore for how the code works
        for o in range(iterations): # calculates the mandelbrot set for a certain number of iterations
            z = z**2 +c 
            abssqr = z.real*z.real + z.imag*z.imag
            if abssqr >= 4:
                break
            if maxorb <= abssqr:
                maxorb = abssqr

        if abs(z) >= abs(complex(2,0)): # if the magnitude of the number is greater than 2 it assumes the function diverges, colours these pixels with the colour function
            '''if o % 2 == 0:
                im.putpixel((x,y), (0,0,0))
            else:'''
            im.putpixel((x,y), (int(100*math.log(o+1))%255,255, int(51 *(math.sqrt(o))))) #exterior colour, ignore for actual logic on how it calculates the set
        else: # if the number doesn't diverge it assumes it converges and is therefore part of the set, colours these pixels black
            im.putpixel((x,y), (0,0,0)) 
im.show()
