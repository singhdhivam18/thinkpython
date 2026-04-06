def read_txt(file):
    fin=open(file,'r')
    empty_list=[]
    for word in fin:
        line=word.strip()
        #2 way to add the word to list
        empty_list=empty_list+[line]
        #empty_list.append(line)
        
    return empty_list
result=read_txt('word.txt')
print(result)