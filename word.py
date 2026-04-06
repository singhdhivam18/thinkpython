def dictinword():
    dictword=['apple','cat','dog','hat']
    new_dict=dict()
    
    for word in dictword:
        keyword=word.strip() 
        if  keyword not in new_dict:
            for index in range(0,1):
                value=ord(keyword[index])
            new_dict[keyword]=value
    print(new_dict)
dictinword()
