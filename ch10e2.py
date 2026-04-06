def cumsum(t):
    total=0
    newlist=[]

    for i in t:
        total +=i
        newlist.append(total)
        
    print(newlist)
        
        
cumsum([1,2,3])
