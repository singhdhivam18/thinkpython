def angram_set():
    list_word=read_txt('word2.txt')
    len_list=len(list_word)
    my_dict={}
    for word in list_word:
        delimiter=''
        keys= delimiter.join(sorted(word))
        if keys in my_dict:
            my_dict[keys].append(word)

        else:
            new_list=[]
            new_list.append(word)
            my_dict[keys]=new_list
    values_list=[]
    for values in my_dict.values():
        '''we can use sorted keyword for the frame in the longer to smaller order
        using sorted with the reverse=True is ascending false is desending '''
        values_list.append(values)
    
    return sorted(values_list,key=lambda inp: len(inp),reverse=True),my_dict

def read_txt(file):
    fin=open(file,'r')
    ans_list=[]
    for word in fin:
        line=word.strip()
        #2 way to add the word to list
        ans_list=ans_list+[line]
        #empty_list.append(line)
        
    return ans_list
angram_set()
def print_ans():
    valuesans,dictionary=angram_set()
    print(valuesans)
print_ans()
