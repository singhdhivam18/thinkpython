def invert_dict(d):
    inverse=dict()
    for key in d:
        val=d.setdefault(key,2)
        if val not in inverse:
            inverse[val]=[key]
        else:
            inverse[val].append(key)
    print(inverse)
invert_dict({'p':1,'a':1,'r':2,'o':1,'t':1})

