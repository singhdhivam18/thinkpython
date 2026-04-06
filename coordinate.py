import copy
class point:
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    '''def __str__(self):
        return '(%g,%g)' % (self.x,self.y)'''
blank=point(10.2)
print(blank)
'''
class rectangle:
    height=0.0
    width=0.0
    corner=point()
box=rectangle()
box.height=100.0
box.width=200.0
box.corner.x=2.0
box.corner.y=3.0


def print_point(p):
    print('(%g,%g)' % (blank.x,blank.y))
print_point(blank)

def find_center(rect):
    p = point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p#return the objcetor innstance
centre=find_center(box)
print_point(centre)
box.width=box.width+50#object are mutable
print(box.width)
p1=point()
p1.x=1.0
p1.y=.20

box2=copy.copy(box)
if box2.width == box.width:#the object are diffrent so false but arritube in that are same so True
    print('true')
else:
    print('false')'''
