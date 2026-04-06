import math
import sys
epsilon=sys.float_info.epsilon
def mysqrt(a,x):
    
    while True:
        y=(x+a/x)/2
        if abs(y-x)< epsilon:
            break
        x=y
    return abs(x)


def test_square_root():
    print("a","\t","mysqrt(a)","\t","math.sqrt(a)","\t","diff")
    print("-","\t","---------","\t","------------","\t","---")
    for a in range(1,10):
        
        fun_sqrt=mysqrt(float(a),float(a/2))
        imp_sqrt=math.sqrt(a)
        diff=abs(fun_sqrt-imp_sqrt)
        print(float(a),"\t",fun_sqrt,"\t",imp_sqrt,"\t",diff)
    
test_square_root()

