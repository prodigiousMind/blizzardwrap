#!/usr/bin/env python3


# class for multitap/phone keypad

class multitap:

    def __init__(self, string):
        self.string = " ".join(string)
        self.tappy = {
            ' ': '0',
            'A': '2',
            'B': '22',
            'C': '222',
            'D': '3',
            'E': '33',
            'F': '333',
            'G': '4',
            'H': '44',
            'I': '444',
            'J': '5',
            'K': '55',
            'L': '555',
            'M': '6',
            'N': '66',
            'O': '666',
            'P': '7',
            'Q': '77',
            'R': '777',
            'S': '7777',
            'T': '8',
            'U': '88',
            'V': '888',
            'W': '9',
            'X': '99',
            'Y': '999',
            'Z': '9999'
        }

    # for encoding
    def encode(self):
        encoded = []
        eString = self.string.upper()
        _keys = list(self.tappy.keys())
        _values = list(self.tappy.values())
        
        
        for e in eString:
            if e in _keys:
                indx = _keys.index(e)
                encoded.append(_values[indx])
            else:
                encoded.append(e)
        return " ".join(encoded)

    # for decoding
    def decode(self):
        decoded = []
        dString = self.string.split()
        _keys = list(self.tappy.keys())
        _values = list(self.tappy.values())

        for d in dString:
            if d in _values:
                indx = _values.index(d)
                decoded.append(_keys[indx])
            else:
                decoded.append(d)
        return "".join(decoded)

    def help(self):
        return '''
    usage: blizzardwrap --phonecode --encode/--decode "string"
           blizzardwrap -ps -e/-d "string"


           -pc, --phonecode       [phonecode/multi-tap encode or decode]'''