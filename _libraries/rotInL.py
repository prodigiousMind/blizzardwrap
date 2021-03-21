#!/usr/bin/env python3

# class for rot algorithm
class rotInL():
    def __init__(self, string, N, ed):
        self.string = string
        self.N = str(N)
        self.ed = str(ed)

    # for bruteforcing all rot algorithm
    def bruteforce(self):
        for roti in range(27):
            shift = roti

            # if self.ed=='e' ...then call for encoding
            if self.ed == 'e':
                print("".join(list("ROT" + str(roti))))
                # print(colored(cipher(self), color="red", attrs=["dark"]))
                print(self.encode(shift))
                print("\n")

            # if self.ed=='d' ...then call for decoding
            elif self.ed == 'd':

                print("".join(list("ROT" + str(roti))))
                # print(colored(cipher(self), color="red", attrs=["dark"]))
                print(self.decode(shift))
                print("\n")

            else:
                print('Error occured: \nno "' + str(self.ed) + '" argument')

        if self.ed == "e":
            print("".join(list("ROT" + str(47))))
            print(self.encode(47))
            print("\n")

        elif self.ed == 'd':
            print("".join(list("ROT" + str(47))))
            # print(colored(cipher(self), color="red", attrs=["dark"]))
            print(self.decode(47))
            print("\n")

        else:
            print('Error occured: \nno "' + str(self.ed) + '" argument')

    # method for rot N encoding or decoding

    def rotN(self):

        # if self.ed is 'e' then call for encoding
        if self.ed == 'e':
            shift = int(self.N)

            # return shift for encoding
            return self.encode(shift)

        # if self.ed is 'd' then call for decoding
        elif self.ed == 'd':
            shift = int(self.N)

            # return shift for decoding
            return self.decode(shift)

        else:
            print('Error occured: \nno "' + str(self.ed) + '" argument')

    # for encoding
    def encode(self, shift):
        _from = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
        _to = 'PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO'

        PlainStr = " ".join(self.string)
        lowerCase = [l for l in "abcdefghijklmnopqrstuvwxyz"]
        upperCase = [l.upper() for l in lowerCase]
        encoded = []

        if int(shift) == 47:
            for letter in PlainStr:
                for l in letter:

                    if l in _from:
                        indxOfL = _from.index(l)
                        encoded.append(_to[indxOfL])
                    else:

                        encoded.append(l)

        else:

            for item in PlainStr:
                PlainStr = item

                for l in PlainStr:
                    if l in lowerCase:
                        indx = lowerCase.index(l)
                        if (indx + shift) <= len(lowerCase) - 1:
                            indx += shift
                            encoded.append(lowerCase[indx])

                        else:
                            indx = (indx + shift) - (len(lowerCase))
                            encoded.append(lowerCase[indx])


                    elif l in upperCase:
                        indx = upperCase.index(l)
                        if (indx + shift) <= len(upperCase) - 1:
                            indx += shift
                            encoded.append(upperCase[indx])
                        else:
                            indx = (indx + shift) - (len(upperCase))
                            encoded.append(upperCase[indx])

                    else:
                        encoded.append(l)

        # return encoded string
        return "".join(encoded)

    # for decoding
    def decode(self, shift):
        _from = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
        _to = 'PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO'
        EncodedStr = " ".join(self.string)
        lowerCase = [l for l in "abcdefghijklmnopqrstuvwxyz"]
        upperCase = [l.upper() for l in lowerCase]
        decoded = []

        if int(shift) == 47:
            for letter in EncodedStr:
                for l in letter:

                    if l in _to:
                        indxOfL = _to.index(l)
                        decoded.append(_from[indxOfL])
                    else:
                        decoded.append(l)


        else:
            for item in EncodedStr:
                EncodedStr = item

                for l in EncodedStr:
                    if l in lowerCase:
                        indx = lowerCase.index(l)

                        if (indx - shift) >= 0:
                            indx -= shift
                            decoded.append(lowerCase[indx])

                        else:
                            indx = (indx - shift) + (len(lowerCase))
                            decoded.append(lowerCase[indx])


                    elif l in upperCase:
                        indx = upperCase.index(l)
                        if (indx - shift) >= 0:
                            indx -= shift
                            decoded.append(upperCase[indx])
                        else:
                            indx = (indx - shift) + (len(upperCase))
                            decoded.append(upperCase[indx])

                    else:
                        decoded.append(l)

        # return decoding
        return "".join(decoded)

    def help(self):
        return '''
    usage: blizzardwrap --rot X --encode/--decode "string"  [X=0 to 26, 47 & 27 for bruteforce]
           blizzardwrap -r X -e/-d "string"                 [X=0 to 26, 47 & 27 for bruteforce]

           -r X, --rot X            [rotX encode or decode]             X=0 to 26, 47 & 27 for bruteforce4

           To bruteforce:
           -r bf, --rot bf          [rotX bruteforce encode or decode]  No need to specify any rot algorithm
           -r bruteforce         
           -r 27, --rot 27'''

