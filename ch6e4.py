def is_power(a,b):
    if a%b==0 and a/b==b:
        return True
    else: 
        return False
power=int(input("enter the power"))
base=int(input("enter the base"))
result=is_power(power,base)
print(result)

