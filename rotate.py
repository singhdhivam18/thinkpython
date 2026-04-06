def rotate_fun(letter,shift):
    
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

            
            print(chr(shiftedLetterAscii),end=' ')
rotate_fun('IBM',-1)