#!/usr/bin/env python3


import termcolor
import colorama
colorama.init()

# class for hexadecimal
class hexadecimal:
    def __init__(self, string):
        self.string = ' '.join(' '.join(string).split())

    #method for encoding
    def encode(self):
        stn = str(self.string)
        encoded = stn.encode("utf-8").hex()

        # return encoded hexadecimal string
        return "0x"+"".join([encoded[one:one+2] for one in range(0,len(encoded),2)])

    # method for decoding
    def decode(self):
        # error handling
        try:

            # split and then make pair of two
            self.string =''.join(self.string.split())
            stn=str(self.string) if self.string[1]!="x" else self.string[2:]
            
            stn = ' '.join([stn[e:e + 2] for e in range(0, len(str(stn)), 2)])
            temp = bytes.fromhex(stn)
            temp = temp.decode('ascii')
            decoded = temp

            # return decoded string
            return decoded

        except:
            # throw an exception
            return termcolor.colored(text="Can't decode non-hexadecimal string", color='red')

    def help(self):
        return '''
    usage: blizzardwrap --hexadecimal --encode/--decode "string"               
           blizzardwrap -hx -e/-d "string"

           -hx, --hexadecimal        [hexadecimal encode or decode]
           '''


# class for hexcode
class hexcode:
    def __init__(self, string):
        self.string = ''.join(' '.join(string).split())

    # method for encoding
    def encode(self):

        # error handling
        try:
            stn = str(self.string)
            temp = int(stn, base=16)
            encoded = temp

            # return encoded string
            return encoded

        #throw an exception
        except:
            return str(termcolor.colored(text="Input must be hexadecimal number", color='red'))+'\nexample: blizzardwrap -hc -e ' +str(termcolor.colored(text="abcdef1234567890", color="blue"))



    # method for decoding
    def decode(self):
        stn = self.string

        try:
            # check if the string is digit or not
            if stn.isdigit():
                decoded = hex(int(stn))

                # return decoded string
                return decoded
            else:
                return termcolor.colored(text="Input must be a hexcode", color="red")

        # throw an exception
        except:
            return termcolor.colored(text="Error Occured make sure you type the correct hexcode", color="red")

    def help(self):
        return '''
    usage: blizzardwrap --hexcode --encode/--decode "string"               
           blizzardwrap -hc -e/-d "string"

           -hc, --hexcode        [hexcode encode or decode]
           '''


#class for binary
class binary:
    def __init__(self, string):
        self.string = ' '.join(' '.join(string).split())

    # method for encoding
    def encode(self):
        try:
            stn = str(self.string)
            binary = []

            temp = list(stn)
            for e in temp:
                for each in e:
                    # can be done like this
                    # binary.append(format(ord(each),'b')) if len(format(ord(each), 'b'))==8 else binary.append('{:0>8}'.format(format(ord(each),'b')))

                    # adding '0' padding for making length equal to eight
                    binary.append(format(ord(each), 'b')) if len(format(ord(each), 'b')) == 8 else binary.append(str(0) * (8 - len(format(ord(each), 'b'))) + str(format(ord(each), 'b')))
            encoded = ' '.join(binary)

            # return encoded string
            return encoded

        # throw an exception
        except:
            return termcolor.colored(text="There is an error in your command", color="red")

    # method for decofing
    def decode(self):
        try:
            stn = str(self.string).split()
            # nested function
            def getMeThat(binDump):
                string = int(binDump, 2)

                # return
                return string

            bin_data = stn

            binWpad = []
            # iterate...
            for item in bin_data:

                if len(item) == 8:
                    binWpad.append(item)
                elif 8 > len(item):
                    # if length smaller than 8 ...add padding
                    binWpad.append('{:0>8}'.format(item))
                else:

                    bin_data = ''.join(item)
                    # start from index to the last one but increment by 8...we have added the padding
                    for bit in range(0, len(bin_data), 8):
                        _byte = bin_data[bit:bit + 8]
                        binWpad.append(_byte)


            str_data = ''

            for one in binWpad:
                temp_data = one

                # call the function and save the return value in a variable
                decDump = getMeThat(temp_data)
                str_data = str_data + chr(decDump)
            decoded = str_data

            # return decoded value
            return decoded

        # throw an exception
        except:
            return termcolor.colored(text="Input must be a binary number", color="red")

    def help(self):
        return '''
    usage: blizzardwrap --binary --encode/--decode "string"               
           blizzardwrap -bin -e/-d "string"

           -bin, --binary        [binary encode or decode]
           '''


# class for binary <=> hexadecimal conversion
class binNhex:
    def __init__(self, string):
        self.string=string

    # binary to hexadecimal conversion
    def bin2hex(self):
        try:
            # iterate...
            for each in self.string:
                for e in each:

                    # double check if the passed input a binary or not
                    if str(e) in ['0','1',' ']:
                        pass
                    else:
                        # if not return this
                        return termcolor.colored(text="Input must be a binary number", color="red")
            else:
                # if it is a binary number then convert
                binDump = binary(self.string).decode()
                binDump = binDump.split()

                # return hexadecimal value of passed binary
                return hexadecimal(binDump).encode()
        # throw an exception
        except:
            return termcolor.colored(text="Input must be a binary number", color="red")

    # hexadecimal to binary conversion
    def hex2bin(self):
        self.string=''.join(''.join(self.string).split())
        stn=self.string

        # pair of two
        self.string=[stn[e:e+2] for e in range(0, len(str(stn)),2)]
        

        try:
            for each in self.string:
                if len(each)==2:
                # if each is not a hex representation...the our exception will be executed...
                    if int(each, 16):
                        pass
                    else:
                        pass
                else:
                    return termcolor.colored(text="Can't decode non-hexadecimal string", color="red")


            else:
                hexDump = hexadecimal(self.string).decode()
                hexDump = hexDump.split()
                hexDump = binary(hexDump).encode()

                # return binary number of passed hexadecimal string
                return hexDump

        # throw an exception
        except:
            return termcolor.colored(text="Can't decode non-hexadecimal string", color="red")


    def help(self):
        return '''
    usage: blizzardwrap --bin2hex "string" or blizzardwrap -b2h               
           blizzardwrap --hex2bin "string" or blizzardwrap -h2b

           -b2h, --b2h         [binary to hexadecimal string]  input string must be binary
           -h2b, --h2b         [hexadecimal to binary string]  input string must be hex string
           '''
