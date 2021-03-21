#!/usr/bin/env python3

# class wigwag


class wigwag:
    def __init__(self, string):
        self.string = " ".join(string)
        self.translator = {
            'A': '22',
            'B': '2112',
            'C': '121',
            'D': '222',
            'E': '12',
            'F': '2221',
            'G': '2211',
            'H': '122',
            'I': '1',
            'J': '1122',
            'K': '2121',
            'L': '221',
            'M': '1221',
            'N': '11',
            'O': '21',
            'P': '1212',
            'Q': '1211',
            'R': '211',
            'S': '212',
            'T': '2',
            'U': '112',
            'V': '1222',
            'W': '1121',
            'X': '2122',
            'Y': '111',
            'Z': '2222'
        }

    # for encoding
    def encode(self):
        
        _keys = list(self.translator.keys())
        _values = list(self.translator.values())
        encodedS = []

        for _each in self.string:
            _each = _each.upper()
            
            if _each in _keys:
                indx = _keys.index(_each)
                encodedS.append(_values[indx])
                
            else:
                encodedS.append(_each)
                
        return " ".join(encodedS)

    # for decoding
    def decode(self):
        
        self.string=self.string.split()
        _keys = list(self.translator.keys())
        _values = list(self.translator.values())
        decodedS = []

        for _each in self.string:
            
            if _each in _values:                
                indx = _values.index(_each)
                decodedS.append(_keys[indx])
                
            else:                
                decodedS.append(_each)

        return "".join(decodedS)

    def help(self):
        
        return '''
    usage: blizzardwrap --wigwag --encode/--decode "string"
           blizzardwrap --ww -e/-d "string"

           -ww, --wigwag        [wigwag encode or decode]'''



