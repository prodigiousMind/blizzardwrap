#!/usr/bin/env python3


class urlShredder():
    def __init__(self, string, whto):

        self.string=string
        self.whto=whto
        self.finalEncoded=[]
        self.finalDecoded=[]
        # a dictionary that'll work as a translator
        self.translator={
            ' ': '%20',
            '!': '%21',
            '"': '%22',
            '#': '%23',
            '$': '%24',
            '%': '%25',
            '&': '%26',
            "'": '%27',
            '(': '%28',
            ')': '%29',
            '*': '%2A',
            '+': '%2B',
            ', ': '%2C',
            '-': '%2D',
            '.': '%2E',
            '/': '%2F',
            '0': '%30',
            '1': '%31',
            '2': '%32',
            '3': '%33',
            '4': '%34',
            '5': '%35',
            '6': '%36',
            '7': '%37',
            '8': '%38',
            '9': '%39',
            ':': '%3A',
            ';': '%3B',
            '<': '%3C',
            '=': '%3D',
            '>': '%3E',
            '?': '%3F',
            '@': '%40',
            'A': '%41',
            'B': '%42',
            'C': '%43',
            'D': '%44',
            'E': '%45',
            'F': '%46',
            'G': '%47',
            'H': '%48',
            'I': '%49',
            'J': '%4A',
            'K': '%4B',
            'L': '%4C',
            'M': '%4D',
            'N': '%4E',
            'O': '%4F',
            'P': '%50',
            'Q': '%51',
            'R': '%52',
            'S': '%53',
            'T': '%54',
            'U': '%55',
            'V': '%56',
            'W': '%57',
            'X': '%58',
            'Y': '%59',
            'Z': '%5A',
            '[': '%5B',
            '\\': '%5C',
            ']': '%5D',
            '^': '%5E',
            '_': '%5F',
            '`': '%60',
            'a': '%61',
            'b': '%62',
            'c': '%63',
            'd': '%64',
            'e': '%65',
            'f': '%66',
            'g': '%67',
            'h': '%68',
            'i': '%69',
            'j': '%6A',
            'k': '%6B',
            'l': '%6C',
            'm': '%6D',
            'n': '%6E',
            'o': '%6F',
            'p': '%70',
            'q': '%71',
            'r': '%72',
            's': '%73',
            't': '%74',
            'u': '%75',
            'v': '%76',
            'w': '%77',
            'x': '%78',
            'y': '%79',
            'z': '%7A',
            '{': '%7B',
            '|': '%7C',
            '}': '%7D',
            '~': '%7E',
            'ˆ': '%CB%86',
            '˜': '%CB%9C',
            'š': '%C5%A1',
            'œ': '%C5%93',
            'ž': '%C5%BE',
            'Ÿ': '%C5%B8',
            '¡': '%C2%A1',
            '¢': '%C2%A2',
            '£': '%C2%A3',
            '¤': '%C2%A4',
            '¥': '%C2%A5',
            '¦': '%C2%A6',
            '§': '%C2%A7',
            '¨': '%C2%A8',
            '©': '%C2%A9',
            'ª': '%C2%AA',
            '«': '%C2%AB',
            '¬': '%C2%AC',
            '®': '%C2%AE',
            '¯': '%C2%AF',
            '°': '%C2%B0',
            '±': '%C2%B1',
            '²': '%C2%B2',
            '³': '%C2%B3',
            '´': '%C2%B4',
            'µ': '%C2%B5',
            '¶': '%C2%B6',
            '·': '%C2%B7',
            '¸': '%C2%B8',
            '¹': '%C2%B9',
            'º': '%C2%BA',
            '»': '%C2%BB',
            '¼': '%C2%BC',
            '½': '%C2%BD',
            '¾': '%C2%BE',
            '¿': '%C2%BF',
            'À': '%C3%80',
            'Á': '%C3%81',
            'Â': '%C3%82',
            'Ã': '%C3%83',
            'Ä': '%C3%84',
            'Å': '%C3%85',
            'Æ': '%C3%86',
            'Ç': '%C3%87',
            'È': '%C3%88',
            'É': '%C3%89',
            'Ê': '%C3%8A',
            'Ë': '%C3%8B',
            'Ì': '%C3%8C',
            'Í': '%C3%8D',
            'Î': '%C3%8E',
            'Ï': '%C3%8F',
            'Ð': '%C3%90',
            'Ñ': '%C3%91',
            'Ò': '%C3%92',
            'Ó': '%C3%93',
            'Ô': '%C3%94',
            'Õ': '%C3%95',
            'Ö': '%C3%96',
            '×': '%C3%97',
            'Ø': '%C3%98',
            'Ù': '%C3%99',
            'Ú': '%C3%9A',
            'Û': '%C3%9B',
            'Ü': '%C3%9C',
            'Ý': '%C3%9D',
            'Þ': '%C3%9E',
            'ß': '%C3%9F',
            'à': '%C3%A0',
            'á': '%C3%A1',
            'â': '%C3%A2',
            'ã': '%C3%A3',
            'ä': '%C3%A4',
            'å': '%C3%A5',
            'æ': '%C3%A6',
            'ç': '%C3%A7',
            'è': '%C3%A8',
            'é': '%C3%A9',
            'ê': '%C3%AA',
            'ë': '%C3%AB',
            'ì': '%C3%AC',
            'í': '%C3%AD',
            'î': '%C3%AE',
            'ï': '%C3%AF',
            'ð': '%C3%B0',
            'ñ': '%C3%B1',
            'ò': '%C3%B2',
            'ó': '%C3%B3',
            'ô': '%C3%B4',
            'õ': '%C3%B5',
            'ö': '%C3%B6',
            '÷': '%C3%B7',
            'ø': '%C3%B8',
            'ù': '%C3%B9',
            'ú': '%C3%BA',
            'û': '%C3%BB',
            'ü': '%C3%BC',
            'ý': '%C3%BD',
            'þ': '%C3%BE',
            'ÿ': '%C3%BF',
            'Ž': '%C5%BD',
            'Œ': '%C5%92',
            'Š': '%C5%A0',
            'ƒ': '%C6%92',
            '™': '%E2%84',
            '›': '%E2%80',
            '‘': '%E2%80%98',
            '’': '%E2%80%99',
            '“': '%E2%80%9C',
            '”': '%E2%80%9D',
            '•': '%E2%80%A2',
            '–': '%E2%80%93',
            '—': '%E2%80%94',
            '‚': '%E2%80%9A',
            '„': '%E2%80%9E',
            '…': '%E2%80%A6',
            '†': '%E2%80%A0',
            '‡': '%E2%80%A1',
            '‰': '%E2%80%B0',
            '‹': '%E2%80%B9',
        }


    # method for encoding
    def encode(self):
        self.string = " ".join(self.string)
        if self.whto == "h":
            for each in self.string:
                if not str(each).isalnum():
                    if str(each) in self.translator.keys():
                        self.finalEncoded.append(self.translator[each])
                    else:
                        self.finalEncoded.append(each)
                else:
                    self.finalEncoded.append(each)

            return "".join(self.finalEncoded)
        elif self.whto == "f":
            for each in self.string:
                if str(each) in self.translator.keys():
                    self.finalEncoded.append(self.translator[each])
                else:
                    self.finalEncoded.append(each)

            return "".join(self.finalEncoded)
        else:
            return self.help()
        
    # method for decoding
    def decode(self):

        self.string = " ".join(self.string)
        # for now just exclude the index 0 as string is gonna' be split with '%'
        temp = self.string.split("%")[1:]
        # list of all keys in translator
        _keys = list(self.translator.keys())
        # list of all values in translator
        _values = list(self.translator.values())
        #
        indx=0

        #nested function
        def _chck(each):
            nonlocal indx
            # check if the length is less than 2 or not

            if len(each)>=2 and indx < len(temp):
                # taking only first two indexes
                
                each1 = '%' + str(each)[:2].upper()
                
                # could have done the other way ... but by doing this its way easier
                if '%'+str(temp[indx])=="%E2" and temp[indx+1:] and temp[indx+2:]:

                    each3='%'+str(temp[indx]).upper()+'%'+str(temp[indx+1]).upper()+'%'+str(temp[indx+2]).upper()[:2]
                    
                    exceptions=['%E2%80%98',
                                '%E2%80%99',
                               '%E2%80%9C',
                               '%E2%80%9D',
                               '%E2%80%A2',
                               '%E2%80%93',
                               '%E2%80%94',
                               '%E2%80%9A',
                               '%E2%80%9E',
                               '%E2%80%A6',
                               '%E2%80%A0',
                               '%E2%80%A1',
                               '%E2%80%B0',
                               '%E2%80%B9']
                    if each3 in exceptions:

                        indxOf = _values.index(each3.upper())

                        self.finalDecoded.append(_keys[indxOf])
                        self.finalDecoded.append(temp[indx + 2][2:] if temp[indx + 2][2:] else '')
                        # increase by 3
                        indx += 3
                        # first time in 3rd index
                        return '13'

                elif each1 in self.translator.values():
                    #if each1 in values then store the index in a variable
                    indxOf = _values.index(each1)
                    #append the key of that value in decoded list
                    self.finalDecoded.append(_keys[indxOf])
                    #append the other indexes too
                    self.finalDecoded.append(temp[indx][2:] if temp[indx][2:] else '')
                    #increase the indx by one as we get our value in first time
                    indx+=1
                    #return with code '11' as we get it first time in first index
                    return '11'

                else:
                    # check if indx+1 exist or not
                    if temp[indx+1:]:
                        #if exist check for its length
                        if len(temp[indx+1])>=2:
                            # take out only first two values
                            each2= each1 +'%'+str(temp[indx+1][0:2]).upper()

                            if each2 in self.translator.values():
                                # if each2 exist append it with its index key
                                indxOf = _values.index(each2)
                                self.finalDecoded.append(_keys[indxOf])
                                # append other indexes too
                                self.finalDecoded.append(temp[indx+1][2:] if temp[indx+1][2:] else '')
                                # increase indx by 2 here as we get our value in second time
                                indx+=2
                                # return code 12 (first time in second)
                                return '12'

                            #check whether or not only (indx+1) in values or not
                            elif '%'+str(temp[indx+1]).upper() in self.translator.values():
                                #if it is then append
                                indxOf = _values.index('%'+str(temp[indx+1]).upper())
                                self.finalDecoded.append('%'+str(temp[indx])+_keys[indxOf])
                                self.finalDecoded.append(temp[indx + 1][2:] if temp[indx + 1][2:] else '')
                                indx += 2
                                return '12'
                            # if not exist
                            else:
                                # check indx+2 exist or not
                                if temp[indx+2:]:
                                    #if exist check or length
                                    if len(temp[indx+2])>=2:
                                        each3=each2+'%'+str(temp[indx+2][0:2]).upper()

                                        #check each3 in values or not
                                        if each3 in self.translator.values():
                                            # if it is then append
                                            indxOf = _values.index(each3)
                                            self.finalDecoded.append(_keys[indxOf])
                                            self.finalDecoded.append(temp[indx + 2][2:] if temp[indx + 2][2:] else '')
                                            # return by 3
                                            indx+=3
                                            # '13' (first time but in 3rd index)
                                            return '13'
                                        # check for indx+2 existence
                                        elif '%'+str(temp[indx+2]).upper() in self.translator.values():
                                            # if exist then append
                                            indxOf = _values.index('%'+str(temp[indx+2]).upper())
                                            self.finalDecoded.append('%'+str(temp[indx])+'%'+str(temp[indx+1])+_keys[indxOf])
                                            self.finalDecoded.append(temp[indx + 2][2:] if temp[indx + 2][2:] else '')
                                            # increase by 3
                                            indx += 3
                                            # first time in 3rd index
                                            return '13'

                                        # if none of them could be decoded
                                        #then just append all three
                                        else:
                                            self.finalDecoded.append('%'+str(temp[indx])+'%'+str(temp[indx+1])+'%'+str(temp[indx+2]))
                                            indx+=3
                                            # (no match not even in third time)
                                            return '03'

                                    else:
                                        # less than 2 length
                                        self.finalDecoded.append('%' + str(temp[indx]) + '%' + str(temp[indx + 1])+'%'+str(temp[indx+2]))
                                        indx+=3
                                        # (no match not even in third time)
                                        return '03'
                                else:

                                    self.finalDecoded.append('%'+str(temp[indx])+'%'+str(temp[indx+1]))
                                    #increase by 2
                                    indx+=2
                                    # (no match not even in second time)
                                    return '02'

                        else:
                            # less than 2 length
                            self.finalDecoded.append('%'+str(temp[indx])+'%'+str(temp[indx+1]))
                            indx+=2
                            # (no match not even in second time)
                            return '02'
                    else:
                        self.finalDecoded.append('%'+str(temp[indx]))
                        #increase by 1
                        indx+=1
                        # (no match)
                        return '01'
            else:
                # less than 2 length
                self.finalDecoded.append('%'+str(temp[indx]))
                indx+=1
                return '01'

        # iterate...
        while indx<len(temp):
            each=temp[indx]
            each=str(each)
            # calling the nested function by passing each as a paramater
            _chck(each)

        # take care of the first index left
        self.finalDecoded.insert(0,self.string.split("%")[0])

        # in the end return decoded string
        return "".join(self.finalDecoded)


    def help(self):
        return '''
    usage: blizzardwrap --url f/h --encode/--decode "string"               
           blizzardwrap -u f/h -e/-d "string"

           -u f, --url f       [URL encode or decode]
                               with 'f'...each character will be encoded
                                
           -u h, --url h       [URL encode or decode]
                               with 'h'...only non-alphanumeric character will be encoded'''

