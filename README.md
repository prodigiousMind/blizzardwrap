

     _     _ _                      _                          
    | |__ | (_)__________ _ _ __ __| |_      ___ __ __ _ _ __  
    | '_ \| | |_  /_  / _` | '__/ _` \ \ /\ / / '__/ _` | '_ \ 
    | |_) | | |/ / / / (_| | | | (_| |\ V  V /| | | (_| | |_) |
    |_.__/|_|_/___/___\__,_|_|  \__,_| \_/\_/ |_|  \__,_| .__/ 
                                                        |_|    
                                        

# blizzardwrap
BlizzardWrap - is an open-source tool for encoding and decoding written in python3
and can be used for encoding or decoding in several formats.
like url,htmlentities,binary,hexadecimal,hexcode,rot,base64,base32,base16,base85,binary2hex,hex2binary encoding or decoding.


How to install?
you can simply clone this whole repository and use it.
or you can download it in a compressed file format.

After installing?
python3 -m pip install -r requirement.txt   (for linux and macOS)
Or
python -m pip install -r requirement.txt    (for windows)

OR Just Run setup.py
run setup.py by:
python3 setup.py


python3 blizzardwrap.py -h
for more help type:
python3 blizzardwrap.py [argument] -h
example: python3 blizzardwrap.py --url -h

usage: blizzardwrap.py [arguments] [--encode/--decode] OR [-e/-d] "[string]"
                                                                                                              
Example: blizzardwrap.py --url --encode "blizzardwrap"                                                        
         blizzardwrap.py --rot 13 --decode  "oyvmmneqjenc"                                                    
type: blizzardwrap -h [argument]    (for more help)

blizzardwrap

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
  
  -e, --encode          encode 
  -d, --decode          decode 
  
  
