def rotate_fun(letter,shift):
        empty_list=[]
        lenght_letter=len(letter)-1
        for i in letter:
            
            minUpCase = 65
            maxUpCase = 90
            minLowCase = 97
            maxLowCase = 122

            letterAscii = ord(i)
            isUpperCase = False
            isLowerCase = False
            if letterAscii >= minUpCase and letterAscii <= maxUpCase:
                isUpperCase = True
            
            if letterAscii >= minLowCase and letterAscii <= maxLowCase:
                isLowerCase = True

            shiftedLetterAscii = letterAscii + shift
            if isUpperCase:
                 while shiftedLetterAscii > maxUpCase and shift > 0:
                    shiftedLetterAscii = shiftedLetterAscii - 26
                 while shiftedLetterAscii < minUpCase and shift < 0:
                      shiftedLetterAscii = shiftedLetterAscii + 26

            if isLowerCase:
                 while shiftedLetterAscii > maxLowCase and shift > 0:
                    shiftedLetterAscii = shiftedLetterAscii - 26
                 while shiftedLetterAscii < minLowCase and shift < 0:
                      shiftedLetterAscii = shiftedLetterAscii + 26 
            letter_chr=chr(shiftedLetterAscii)
            for i in letter_chr:
                 empty_list.append(i)
            delemiter=''
            result=delemiter.join(empty_list)
        return result
def word_list(filename):
     fin=open(filename,'r')
     dict_empty={}
     for word in fin:
          line=word.strip()
          rotatedWord=rotate_fun(line,5)
          
          if rotatedWord not in dict_empty:
               dict_empty[rotatedWord]=1
          else:
               dict_empty[rotatedWord]=1
               
               
     print(dict_empty)
word_list('word.txt')
          
    
               
