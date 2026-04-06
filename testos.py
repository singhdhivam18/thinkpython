'''parameter '''
import time
middlelist=[]
def binary_search(inp_list,first,last,key):
    print('binary search:',first,last)
    middle=(first+last)//2
    #print(middle)
    
    #middlelist.append(middle)
    #print(middlelist)
    #duplicate_ans=has_duplicate(middlelist)
    #if duplicate_ans==True:
     #   return False
    if key==inp_list[middle]:
        print(key)
        return True
    elif middle==first and last-first==1:
        return False
    elif inp_list[middle] >key:
        return binary_search(inp_list,first,middle,key)
        
    else:
        return binary_search(inp_list,middle,last,key)
    


tem_list=[5]
sorted_list=sorted(tem_list)
print(sorted_list)
first=0
last=len(tem_list)
print(last)
key=5

'''def has_duplicate(s):
    count=0
    len_list=len(s)
    for i in range(len_list):
        j=i+1
        while j<len_list:
            if s[i]==s[j]:
                count=count+1
            j=j+1
    if count>=1:
        return True
    else:
        return False

print(binary_search(sorted_list,first,last,key))
timetaken=time.process_time()
print(timetaken)'''        
if len(sorted_list)==0:
    print('false')
else:
    print(binary_search(sorted_list,first,last,key))