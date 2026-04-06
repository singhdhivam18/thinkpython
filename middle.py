def middle_fun(t):
    length_list=len(t)
    del t[0]
    del t[-1]
    print(t)
middle_fun([1,2,3,4,8,9])
