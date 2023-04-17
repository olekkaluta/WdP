from vpython import *
from vpython import color, points, vector

p =[]

cw =0.0

cr=-0.2
ci=-0.0
cj=-0.2
ck=0.7

zoom = 1
a = 0.0
b = 0.0
c = 0.0

maxIter = 20
pointMin = 14

mandel = 1

for k in range(-200,200,2):
    for j in range(-200,200,2):
        for i in range(-200,200,2):

            w = cw
            x =a + i/(100.0 * zoom)
            y =b + j/(100.0 * zoom)
            z =c + k/(100.0 * zoom)
		
            if mandel == 1:
                cr = x
                ci = y
                cj = z
                ck = w
				
            iter = 0
			
            dist = 0

            while dist < 4 and iter < maxIter:
                tem = x+x
                x = x*x-y*y-z*z-w*w+cr
                y = tem*y + ci
                z = tem*z + cj
                w = tem*w + ck
    
                iter += 1
                dist = x*x +y*y + z*z + w*w

            if iter >= pointMin  and iter <=maxIter-1:
                d=vector(264,63,32)
                Color = color.hsv_to_rgb(d)             
                p=points(pos=(i,j,k),color=Color,shape='square',radius=2,size_units="pixels")
p

while True:
    pass