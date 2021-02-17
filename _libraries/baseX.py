#!/usr/bin/env python3

#importing...
import termcolor
import colorama
import base64


colorama.init()

# class for base64
class Base64:
    def __init__(self, string):
        self.string=' '.join(' '.join(string).split())
    # for encoding
    def encode(self):
        stn=self.string.encode('ascii')

        # return encoded string
        return base64.b64encode(stn).decode('ascii')
    # for decoding
    def decode(self):
        stn=self.string

        # return decoded string
        return base64.b64decode(stn).decode('ascii')

#class for base32
class Base32:
    def __init__(self, string):
        self.string=' '.join(' '.join(string).split())

    def encode(self):
        # for encoding
        stn=self.string.encode('ascii')

        # return encoded string
        return base64.b32encode(stn).decode('ascii')

    def decode(self):
        # for decoding
        stn=self.string

        # return decoded string
        return base64.b32decode(stn).decode('ascii')

#class for base16
class Base16:
    def __init__(self, string):
        self.string=' '.join(' '.join(string).split())

    # for encoding
    def encode(self):
        stn=self.string.encode('ascii')

        # return encoded string
        return base64.b16encode(stn).decode('ascii')

    # for decoding
    def decode(self):
        stn=self.string

        # return decoded string
        return base64.b16decode(stn).decode('ascii')

#class for base85
class Base85:
    def __init__(self, string):
        self.string=' '.join(' '.join(string).split())

    # for encoding
    def encode(self):
        stn = self.string.encode('ascii')

        # return encoded string
        return base64.b85encode(stn).decode('ascii')

    # for decoding
    def decode(self):
        stn = self.string

        # return decoded string
        return base64.b85decode(stn).decode('ascii')


class help:
    def help(self):

        return    '''
    usage: blizzardwrap --base X --encode/--decode "string"  [X=16,32,64,85]
           blizzardwrap -b X -e/-d "string"                  [X=16,32,64,85]

           -b 16, --base 16         [base16 encode or decode]
           -b 32, --base 32         [base32 encode or decode]
           -b 64, --base 64         [base64 encode or decode]
           -b 85, --base 85         [base85 encode or decode]
           '''







class mHelp:
    def help(self):
        return '''
usage: '''+str(termcolor.colored(text="blizzardwrap.py [arguments] [--encode/--decode]OR[-e/-d] \"[string]\"\n\n"
                                                            "Example: blizzardwrap.py --url --encode \"blizzardwrap\"\n"
                                                            "         blizzardwrap.py --rot 13 --decode  \"oyvmmneqjenc\"",
                                                            color="red"))+'\n'+str(termcolor.colored(text="type: blizzardwrap -h [argument]    (for more help)", color="yellow"))+'''\n\n'''+str(termcolor.colored(text=str("blizzardwrap"), color="blue", on_color="on_grey"))+'''

positional arguments:
  string                string to encode or decode

optional arguments:
  -h, --help            show help or exit
  -u, --url             url encode or decode
  
  -r, --rot             rotN encode or decode
                        [0 to 26 & 27,bf,bruteforce]
                        
  -b, --base            baseX encode or decode
                        {16,32,64,85}
                        
  -hc, --hexcode        hexcode encode or decode
  -hx, --hexadecimal    hexadecimal bytes encode or decode
  -bin, --binary        binary encode or decode
  -b2h, --bin2hex       binary to hexadecimal
  -h2b, --hex2bin       hexadecimal to binary
  -html, --htmlcode     html encode or decode
  -mc, --morsecode      morsecode encode or decode
  
  -e, --encode          encode 
  -d, --decode          decode 
'''
