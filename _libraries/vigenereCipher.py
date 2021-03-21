#!/usr/bin/env python3

# class vigenere cipher

class vigyCiphy:

    def __init__(self, string, what, case):
        
        # for case sensitivity
        
        if case == "a":
            self.string = "".join(string).lower()
            self.key = input("Please enter the key/passphrase: ").upper()
            self.passphrase = self.keyGenerator(self.string, self.key, what)
            self.what = what
            
        elif case == "A":
            self.string = "".join(string).upper()
            self.key = input("Please enter the key/passphrase: ").upper()
            self.passphrase = self.keyGenerator(self.string, self.key, what)
            self.what = what
            
        elif case == "aA":
            self.string = "".join(string)
            self.key = input("Please enter the key/passphrase: ").upper()
            self.passphrase = self.keyGenerator(self.string, self.key, what)
            self.what = what

    def operateMe(self):
        
        # call function for encoding/decoding
        if self.what == "e":            
            encoded = self.encode(self.string, self.passphrase)
            return encoded
        
        elif self.what == "d":
            decoded = self.decode(self.string, self.passphrase)
            return decoded
        
        else:
            return self.help()

    def keyGenerator(self, string, key, what):

        # generate key
        key = list(key)

        for num in range(len(string) -
                         len(key)):
            key.append(key[num % len(key)])
            
        for num in range((len(string))):
            if not string[num].isalpha():
                key.insert(num, " ")

        return ("".join(key))

    # encode
    def encode(self, string, key):
        
        ciphy = []
        for num in range(len(string)):
            
            if string[num].isalpha() and string[num].upper() == string[num]:
                
                uniHold = (ord(string[num]) +
                           ord(key[num])) % 26
                uniHold += ord('A')
                ciphy.append(chr(uniHold))
                
            elif string[num].isalpha() and string[num].lower() == string[num]:
                
                uniHold = (ord(string[num].upper()) +
                           ord(key[num])) % 26
                uniHold += ord('A')
                ciphy.append(chr(uniHold).lower())
                
            else:
                ciphy.append(string[num])

        return ("".join(ciphy))

    # decode
    def decode(self, ciphy, key):
        
        deciphy = []
        for num in range(len(ciphy)):
            if ciphy[num].isalpha() and ciphy[num].upper() == ciphy[num]:
                
                uniHold = (ord(ciphy[num]) -
                           ord(key[num]) + 26) % 26
                uniHold += ord('A')
                deciphy.append(chr(uniHold))
            elif ciphy[num].isalpha() and ciphy[num].lower() == ciphy[num]:
                
                uniHold = (ord(ciphy[num].upper()) -
                           ord(key[num]) + 26) % 26
                uniHold += ord('A')
                deciphy.append(chr(uniHold).lower())
            else:
                
                deciphy.append(ciphy[num])

        return ("".join(deciphy))

    def help(self):
        
        return '''
    usage: blizzardwrap --vigenere --encode/--decode "string"
           blizzardwrap --vc -e/-d "string"

           [NOTE]: Key/Passphrase required 

           -vc 0, --vigenere        [vigenere cipher encode/decode, case sensitivity on]
           -vc a, --vigenere        [vigenere cipher encode/decode, lower case]
           -vc A, --vigenere        [vigenere cipher encode/decode, upper case]'''


