def nested_list(t):
    total=0
    for i in t:
        if isinstance(i,list):
           
            currenti=i
            total=total+sum(currenti)
            
        else:
             total= total+i
             

    print(total)


nested_list( [[1, 2], [3], [4, 5, 6]])