import math
class point:
    """x and y"""
class circle:
    """radius"""
blank=point()
cric=circle()
blank.x=69.5
blank.y=132.5
cric.radius=75
def point_in_circle(blank,cric):
    diameter=cric.radius*2
    distance=math.sqrt(blank.x**2+blank.y**2)
    print(distance)
    if distance==diameter:
        print("on the circle")
    elif distance<diameter:
        print("in the circle")
    else:
        print("out the circle")
point_in_circle(blank,cric)      
class rectangle():
    """width,heightand conrner""" 
box=rectangle()
box.coner=point()
box.coner.x=5
box.coner.x1=15
box.coner.y=10
box.coner.y1=10
def rect_in_circle(box):
    diameter=cric.radius*2
    distance=math.sqrt((box.coner.x1-box.coner.x)**2+(box.coner.y1-box.coner.y)**2)
    print(distance)
    if distance<=diameter:
        return True
    else:
        return False
print(rect_in_circle(box))
