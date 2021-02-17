#!/usr/bin/env python3

import termcolor
import colorama


colorama.init()

# class for morseCode
class morseCode:
    def __init__(self, string):
        self.string = string

        # list to append the value into
        self.finalEncoded=[]
        self.finalDecoded=[]

        # dict for translation
        self.translator = {
            '0': '-----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            'Á':'.__._',
            'Ä': '._._',
            'Ñ':'__.__',
            'Ü':'..__',
            'É':'.._..',
            'Ö': '___.',
            '"': '._.._. ',
            ':': '___... ',
            ';': '_._._. ',
            '=': '_..._',
            "'":'.____.',
            '.': '.-.-.-',
            '_': '..__._',
            ',': '--..--',
            '?': '..--..',
            '!': '-.-.--',
            '-': '-....-',
            '+':'._._.',
            '/': '-..-.',
            '@': '.--.-.',
            '(': '-.--.',
            ')': '-.--.-',
            ' ': '/'
        }

    # method for encoding
    def encode(self):
        self.string=' '.join(self.string)
        try:
            for code in self.string:
                code=str(code)
                #check and then append
                if code.isalpha() and code.upper() in self.translator.keys():
                    code=code.upper()
                    self.finalEncoded.append(self.translator[code])
                elif code.isdigit():
                    if code in self.translator.keys():
                        self.finalEncoded.append(self.translator[code])
                    else:
                        self.finalEncoded.append(code)
                else:
                    if code in self.translator.keys():
                        self.finalEncoded.append(self.translator[code])
                    else:
                        # if not present then append as it is
                        self.finalEncoded.append(code)

            # return the encoded string
            return ' '.join(self.finalEncoded)

        #throw an exception
        except:
            return termcolor.colored(text="Error occured!\ncheck the string")

    # method for decoding
    def decode(self):
        self.string=''.join(self.string).split()
        _keys = list(self.translator.keys())
        _values = list(self.translator.values())

        try:
            # iterate...
            for code in self.string:
                code=str(code)
                # check and append
                if code in self.translator.values():
                    indxOf=_values.index(code)
                    self.finalDecoded.append(_keys[indxOf])
                else:
                    # if not present then append as it is
                    self.finalDecoded.append(code)

            #return decoded string
            return ''.join(self.finalDecoded)
        #throw an exception
        except:
            return termcolor.colored(text="Error occured!\ncheck the string")


    def help(self):
        return '''
    usage: blizzardwrap --morsecode --encode/--decode "string"  
           blizzardwrap -mc -e/-d "string"                  

           -mc, --morsecode         [morsecode encode or decode]
           '''

