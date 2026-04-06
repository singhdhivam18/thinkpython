def has_duplicate(s):
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
        
ans=has_duplicate([1,2,3])
print(ans)