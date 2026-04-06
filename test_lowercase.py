def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
        
ans=any_lowercase1("AMAN")
print(ans)
print("the return value in string")
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
ans=any_lowercase2("shivam")
print(ans)
print(" the boolean value is assiged to variable and returned")
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        return flag
ans=any_lowercase3("shivam")
print(ans)
print("it check the lower case and here the or opertion performed \n so if one is true then ite return true ")
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
        return flag
ans=any_lowercase4("shivam")
print(ans)


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
ans=any_lowercase5("python")
print(ans)

