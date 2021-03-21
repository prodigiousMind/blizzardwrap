#!/usr/bin/env python3


# class ascii
class Ascii:

    def __init__(self, string):
        self.string=" ".join(string)
        
    def encode(self):
        encodedS=[]
        for _each in self.string:
            try:
                encodedS.append(format(ord(_each)))
            except:
                encodedS.append(_each)
                
        return " ".join(encodedS)
        
        
    def decode(self):
        decodedS=[]
        for _each in self.string:
            try:                
                decodedS.append(format(chr(_each)))
            except:
                decodedS.append(_each)
                
        return " ".join(decodedS)
        
    def help(self):
        return '''
        usage: blizzardwrap --ascii --encode/--decode "string"
           blizzardwrap --ww -e/-d "string"

           -ai, --ascii        [ascii encode or decode]'''
        
    
                
       