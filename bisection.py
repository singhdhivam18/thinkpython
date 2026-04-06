global middlelist
middlelist=[]
global count
count=0
def listinword():
    readed=open('word.txt','r')#read the word file words
    new_list=[]
    for word in readed:
        readword=word.strip()
        if readword not in new_list:
            new_list.append(readword)
    sorted_list=sorted(new_list)#new_list contain the words
    return sorted_list#sorted_list contain sorted in alphabetic

def binary_search(inp_list,first,last,key):
    print('binary search:',first,last)
    middle=(first+last)//2
    if first>=last:
        return False
    elif key==inp_list[middle]:
        print(key)
        return True
    elif inp_list[middle] >key:
        return binary_search(inp_list,first,middle,key)
        
    else:
        return binary_search(inp_list,middle,last,key)
    
def Assignvalues():
    
    sortedlist=listinword()
    print('the bsorted list of words from word file',sortedlist)
    first=0
    last=len(sortedlist)
    TargetValue=input("enter the string to search wether it present or not =")
    Searchresult=binary_search(sortedlist,first,last,TargetValue)
    if Searchresult==True:
        print('found')
    else:
        print('not found')
Assignvalues()


'''def in_bisect():
    ans=False
    Sortedlist=listinword()
    lenghtOflist=len(Sortedlist)
    first=0
    Targetvalue=input("enter the target value to search:")
    middle=(first+lenghtOflist)//2
    for i in range(first,middle+1):
        if Sortedlist[i]==Targetvalue:
            ans=True
            break
    
    if ans==True:
        print('true',Sortedlist[i])
     
    elif ans==False:
        for j in range(middle,lenghtOflist):
            if Sortedlist[j]==Targetvalue:
                print("found in second",Sortedlist[j])
                break
            else: 
                print('not in the word list')
    
in_bisect()'''


    