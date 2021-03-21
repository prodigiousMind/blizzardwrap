#!/usr/bin/env python3


import colorama
import termcolor

# class for A1Z26

colorama.init()

class A1Z26:

    def __init__(self, string):
        self.string=string

    def encode(self):
        _toEncode=" ".join(self.string)
        alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        encodedString=[]

        for each in _toEncode:
        
            if str(each).upper() in alpha:
                indx=alpha.index(str(each).upper())
                # add padding 
                encodedString.append("0"+str(indx+1)+" " if indx<9 else str(indx+1)+" ")

            else:
                encodedString.append(each)

        return "".join(encodedString)





    def decode(self):

        try:
            _toDecode="".join("".join(self.string).split())
            _toDecode=[str(_toDecode[e])+str(_toDecode[e+1]) for e in range(0,len(_toDecode),2)]
            alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            decodedString=[]
            curIn=1

            for each in _toDecode:
                
                if int(each)>0 and int(each)<=26 and str(each).isdigit():
                    decodedString.append(alpha[int(each)-1])
                else:
                    decodedString.append(str(each))
                    
                
                
            return "".join(decodedString)

        except:
            return termcolor.colored("Input string must be a pair of integers (for example: 01 instead of 1)", color="red")




    def help(self):
        return '''
    usage: blizzardwrap --a1z26 --encode/--decode "string"
           blizzardwrap -az -e/-d "string"
           

           -az, --a1z26        [a1z26 encode]
                               [a1z26 decode]  input string must be in pair of two integer from 01 to 26
                               (ie: blizzardwrap -az -d "01 02 03 04 05 06"'''





