#!/usr/bin/env python3

# class atbash

class atbash:

    def __init__(self, string):
        self.string = " ".join(string)
        self._from = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self._to = list("ZYXWVUTSRQPONMLKJIHGFEDCBA")

    # encoding
    def encode(self):
        toEncode = self.string
        encodedString = []

        for each in toEncode:

            if each.islower() and each.upper() in list(self._from):
                indx = self._from.index(each.upper())
                encodedString.append(list(self._to)[indx].lower())
            elif each.isupper() and each in self._from:
                indx = self._from.index(each)
                encodedString.append(list(self._to)[indx])
            else:
                encodedString.append(each)

        return "".join(encodedString)

    # decoding
    def decode(self):
        toDecode = self.string
        decodedString = []

        for each in toDecode:
            if each.islower() and each.upper() in self._to:
                indx = self._to.index(each.upper())
                decodedString.append(self._from[indx].lower())
            elif each.isupper() and each in self._to:
                indx = self._to.index(each)
                decodedString.append(self._from[indx])
            else:
                decodedString.append(each)

        return "".join(decodedString)

    def help(self):
        return '''
    usage: blizzardwrap --atbash --encode/--decode "string"
           blizzardwrap -at -e/-d "string"


           -at, --atbash       [atbash encode or decode]'''