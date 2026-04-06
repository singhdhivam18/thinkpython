def word_list(file,my_word):
    fin=open(file,'r')
    print(my_word)
    for word in fin:
        line=word.strip()
        if  my_word==line:
            return True
    return False
ans=word_list('word.txt','shivam')
print(ans)