"""Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
evaluates it using eval, and prints the result."""
import math
def eval_loop():
    while True:
        value=input("enter the value actually it's str type . \n out of the loop type done")
        if value=='done':
            break
        else:
            print(eval(value))
eval_loop()

class add:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def __add__(self,other):
        ansadd=self.a+other.a
        ansaddb=self.b+other.b
        return printab(ansadd,ansaddb)
def printab(ansa,ansb):
    print(ansa,ansb)
obj1=add(10,2)
obj2=add(20,3)
obj3=obj1+obj2
            