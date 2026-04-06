def find_duplicate(my_dict):
    count=0
    new_dict=dict()
    for keys in my_dict:
        if keys in new_dict:
            count=count+1
        else:
            new_dict[keys]=1
    if count>=1:
        print('duplicate found in dictionary')
    else:
        print('not found')
find_duplicate([1,2,3])#we can pass string and integer values any datatype


        