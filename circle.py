import math
class point:
    x=0.0
    y=0.0
blank=point()
class react:
    width=25000
    height=1105
    corner=point()
box=react()
class circle:
    radius=0.0
    center=point()
value=circle()
value.center.x=150
value.center.y=100
value.radius=75
#value.center.x,value.center.y=float(input("what is the center of circle"))
def point_in_circle(fcircle,fpoint):
    fpoint.x=float(input("what is coordinate x "))
    fpoint.y=float(input('what is coordinate y'))
    
    distance=math.sqrt(((fpoint.x-fcircle.center.x)**2+(fpoint.y-fcircle.center.y)**2))
    print('the distance ',distance)
    if distance<fcircle.radius*2:
        print('the point lies in the circle')
        if distance==fcircle.radius*2:
            print('the point on boundary  circle',)
    else:
        print('out of the  boundary')
point_in_circle(value,blank)
def rect_in_circle(box,value):#sqrt(width+height)<=diameter
    diagonal=math.sqrt(box.width+box.height)
    print(diagonal)
    if diagonal<=2*value.radius:
        print('the reactangle can fit in the circle')
    else:
        print('the rectangle not fit in the circle')
rect_in_circle(box,value)