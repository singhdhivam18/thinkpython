import math
def check_fermat(a,b,c,n):
   if math.pow(a,n)+math.pow(b,n)==math.pow(c,n) and n>2:
      print("Holy smokes, Fermat was wrong!")
   else:
      print("no it don't work")
a=int(input("what is a?"))
b=int(input("what is b?"))
c=int(input("wh at is c"))
n=int(input("wha t is n"))
check_fermat(a,b,c,n)
      
          