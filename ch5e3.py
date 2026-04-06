def is_trinagle(stick1,stick2,stick3):
    if(stick1>stick2+stick3 or stick2>stick1+stick3 or stick3>stick1+stick2 ):
        print("you cannot form a trinagle")
    elif stick1+stick2==stick3 or stick2+stick3==stick1 or stick3+stick1==stick2 :
        print("you can form a trinagle")
    else:
        print("none of them are not true so can't form a trinagle")
def get_lenght():
    stick1=int(input("what is the lenght of stick one only a digit "))
    stick2=int(input("what is the lenght of stick two only a digit "))
    stick3=int(input("what is the lenght of stick three only a digit "))
    is_trinagle(stick1,stick2,stick3)
get_lenght()