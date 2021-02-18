#!/usr/bin/env python3


# Author: prodigiousMind
# youtube: https://www.youtube.com/channel/UCyoQWc93GZRlYl1LL7J5MrQ
# github: https://github.com/prodigiousMind/
#
# blizzardwrap is a CLI (command line interface) tool for encoding and decoding written in python3.
# blizzardwrap supports URL,MorseCode,HTMLEntities,Binary,Hexadecimal,Hexcode,ROT,Base64,Base32,Base16,Base85,Binary2Hex,Hex2Binary encoding & decoding
# read README.md for more.


import sys
import argparse
import termcolor
import colorama
from _libraries.urlShredder import urlShredder
from _libraries.baseX import Base32, Base64, Base16, Base85, help, mHelp
from _libraries.rotInL import rotInL
from _libraries.htmlEntities import html
from _libraries.morseCode import morseCode
from _libraries.biex import hexadecimal, hexcode, binary, binNhex

colorama.init()

# creating argument parser

parser = argparse.ArgumentParser(description=termcolor.colored(text=str("blizzardwrap"), color="yellow"),
                                 usage=termcolor.colored(
                                     text="blizzardwrap.py [arguments] [--encode/--decode]OR[-e/-d] \"[string]\"\n\n"
                                          "Example: blizzardwrap.py --url --encode \"blizzardwrap\"\n"
                                          "         blizzardwrap.py --rot 13 --decode  \"oyvmmneqjenc\"\n"
                                          + str(
                                         termcolor.colored(text="type: blizzardwrap -h [argument]    (for more help)",
                                                           color="blue")),
                                     color="red"), add_help=False)

# adding all argumets

parser.add_argument('-h', '--help', action='store_true', help="show help or exit")
parser.add_argument('-u', '--url', nargs="?", default="h",const=1, help="url encode or decode")
parser.add_argument('-r', '--rot',
                    choices=['bf', 'bruteforce', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                             '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27'],
                    help="rotN encode or decode")
parser.add_argument('-b', '--base', choices=['16', '32', '64', '85'], help="baseX encode or decode")
parser.add_argument('-hc', '--hexcode', action='store_true', help="hexcode encode or decode")
parser.add_argument('-hx', '--hexadecimal', action='store_true', help="hexadecimal bytes encode or decode")
parser.add_argument('-bin', '--binary', action='store_true', help="binary encode or decode")
parser.add_argument('-b2h', '--bin2hex', action='store_true', help="binary to hexadecimal")
parser.add_argument('-h2b', '--hex2bin', action='store_true', help="hexadecimal to binary")
parser.add_argument('-html', '--htmlcode', action='store_true', help="html encode or decode")
parser.add_argument('-mc', '--morsecode', action='store_true', help="morsecode encode or decode")
parser.add_argument('-e', '--encode', action="store_true", help="encode")
parser.add_argument('-d', '--decode', action="store_true", help="decode")
parser.add_argument('string', nargs='*', help="string to encode or decode")

args = parser.parse_args()

# calling methods based on passed arguments

try:
    if len(sys.argv) >= 2:

        if len(sys.argv) == 2 and args.help or len(sys.argv) == 2 and args.string or len(
                sys.argv) and args.string and args.help and args.url=='h':
            print(mHelp().help())


        if args.rot:
            if args.help:
                print(rotInL("0", "0", "0").help())
            elif str(args.rot) == 'bruteforce' or str(args.rot) == 'bf' or str(args.rot) == '27':
                if args.encode:
                    if args.string:
                        rotInL(args.string, 'bf', 'e').bruteforce()
                    else:
                        print("blizzardwrap --rot 27/bf/bruteforce --encode/-e \"" + termcolor.colored(text="string", color="red") +
                              "\"")
                elif args.decode:
                    if args.string:
                        rotInL(args.string, 'bf', 'd').bruteforce()
                    else:
                        print("blizzardwrap --rot 27/bf/bruteforce --decode/-d \"" + termcolor.colored(text="string", color="red") +
                              "\"")
                else:
                    print("blizzardwrap --rot bf/bruteforce", termcolor.colored(text="-e/-d", color="red"),
                          "\"string\"")
            elif str(args.rot).isdigit() and str(args.rot) != '27':
                if args.encode:
                    if args.string:
                        print(rotInL(args.string, str(args.rot), 'e').rotN())
                    else:
                        print("blizzardwrap --rot [num] --encode/-e \"" + termcolor.colored(text="string",
                                                                                                       color="red") +
                              "\"")

                elif args.decode:
                    if args.string:
                        print(rotInL(args.string, str(args.rot), 'd').rotN())
                    else:
                        print("blizzardwrap --rot [num] --decode/-d \"" + termcolor.colored(text="string",
                                                                                                       color="red") +
                              "\"")
                else:
                    print("blizzardwrap --rot [num]", termcolor.colored(text="-e/-d", color="red"), "\"string\"")

            else:
                parser.print_help()

        if args.morsecode:
            if args.help:
                print(morseCode("0").help())

            elif args.encode:
                if args.string:
                    print(morseCode(args.string).encode())
                else:
                    print("blizzardwrap --morsecode --encode/-e \"" + termcolor.colored(text="string",
                                                                                         color="red") +
                          "\"")

            elif args.decode:
                if args.string:
                    print(morseCode(args.string).decode())
                else:
                    print("blizzardwrap --morsecode --decode/-d \"" + termcolor.colored(text="string",
                                                                                         color="red") +
                          "\"")
            else:
                print("blizzardwrap --morsecode", termcolor.colored(text="-e/-d", color="red"),
                      "\"string\"")

        if args.base:
            if args.help:
                print(help().help())

            elif args.base == '64':
                if args.encode:
                    if args.string:
                        print(Base64(args.string).encode())
                    else:
                        print("blizzardwrap --base 64 --encode/-e \"" + termcolor.colored(text="string",
                                                                                            color="red") +
                              "\"")
                elif args.decode:
                    if args.string:
                        print(Base64(args.string).decode())
                    else:
                        print("blizzardwrap --base 64 --decode/-d \"" + termcolor.colored(text="string",
                                                                                            color="red") +
                              "\"")
                else:
                    print("blizzardwrap --base 64", termcolor.colored(text="-e/-d", color="red"),
                          "\"string\"")

            elif args.base == '32':
                if args.encode:
                    if args.string:
                        print(Base32(args.string).encode())
                    else:
                        print("blizzardwrap --base 32 --encode/-e \"" + termcolor.colored(text="string",
                                                                                            color="red") +
                              "\"")
                elif args.decode:
                    if args.string:
                        print(Base32(args.string).decode())
                    else:
                        print("blizzardwrap --base 32 --decode/-d \"" + termcolor.colored(text="string",
                                                                                            color="red") +
                              "\"")
                else:
                    print("blizzardwrap --base 32", termcolor.colored(text="-e/-d", color="red"),
                          "\"string\"")

            elif args.base == '16':
                if args.encode:
                    if args.string:
                        print(Base16(args.string).encode())
                    else:
                        print("blizzardwrap --base 16 --encode/-e \"" + termcolor.colored(text="string",
                                                                                            color="red") +
                              "\"")
                elif args.decode:
                    if args.string:
                        print(Base16(args.string).decode())
                    else:
                        print("blizzardwrap --base 16 --decode/-d \"" + termcolor.colored(text="string",
                                                                                            color="red") +
                              "\"")
                else:
                    print("blizzardwrap --base 16", termcolor.colored(text="-e/-d", color="red"),
                          "\"string\"")


            elif args.base == '85':
                if args.encode:
                    if args.string:
                        print(Base85(args.string).encode())
                    else:
                        print("blizzardwrap --base 85 --encode/-e \"" + termcolor.colored(text="string",
                                                                                            color="red") +
                              "\"")
                elif args.decode:
                    if args.string:
                        print(Base85(args.string).decode())
                    else:
                        print("blizzardwrap --base 85 --decode/-d \"" + termcolor.colored(text="string",
                                                                                            color="red") +
                              "\"")
                else:
                    print("blizzardwrap --base 85", termcolor.colored(text="-e/-d", color="red"),
                          "\"string\"")

        if args.htmlcode:
            if args.help:
                print(html("0").help())
            elif args.encode:
                if args.string:
                    print(html(args.string).encode())
                else:
                    print("blizzardwrap --htmlcode --encode/-e \"" + termcolor.colored(text="string",
                                                                                      color="red") +
                          "\"")
            elif args.decode:
                if args.string:
                    print(html(args.string).decode())
                else:
                    print("blizzardwrap --htmlcode --decode/-d \"" + termcolor.colored(text="string",
                                                                                      color="red") +
                          "\"")
            else:
                print("blizzardwrap --htmlcode", termcolor.colored(text="-e/-d", color="red"),
                      "\"string\"")

        if True:
            if args.hexcode:
                if args.help:
                    print(hexcode("0").help())
                elif args.encode:
                    if args.string:
                        print(hexcode(args.string).encode())
                    else:
                        print("blizzardwrap --hexcode --encode/-e \"" + termcolor.colored(text="hexadecimal number",
                                                                                            color="red") +
                              "\"")
                elif args.decode:
                    if args.string:
                        print(hexcode(args.string).decode())
                    else:
                        print("blizzardwrap --hexcode --decode/-d \"" + termcolor.colored(text="hexadecimal number",
                                                                                            color="red") +
                              "\"")
                else:
                    print("blizzardwrap --hexcode", termcolor.colored(text="-e/-d", color="red"),
                          "\"hexadecimal number\"")

            elif args.hexadecimal:
                if args.help:
                    print(hexadecimal("0").help())
                elif args.encode:
                    if args.string:
                        print(hexadecimal(args.string).encode())
                    else:
                        print("blizzardwrap --hexadecimal --encode/-e \"" + termcolor.colored(text="string",
                                                                                           color="red") +
                              "\"")

                elif args.decode:
                    if args.string:
                        print(hexadecimal(args.string).decode())
                    else:
                        print("blizzardwrap --hexadecimal --decode/-d \"" + termcolor.colored(text="string",
                                                                                           color="red") +
                              "\"")
                else:
                    print("blizzardwrap --hexadecimal", termcolor.colored(text="-e/-d", color="red"),
                          "\"string\"")

            elif args.binary:
                if args.help:
                    print(binary("0").help())
                elif args.encode:
                    if args.string:
                        print(binary(args.string).encode())
                    else:
                        print("blizzardwrap --binary --encode/-e \"" + termcolor.colored(text="string",
                                                                                           color="red") +
                              "\"")
                elif args.decode:
                    if args.string:
                        print(binary(args.string).decode())
                    else:
                        print("blizzardwrap --binary --decode/-d \"" + termcolor.colored(text="string",
                                                                                           color="red") +
                              "\"")
                else:
                    print("blizzardwrap --binary", termcolor.colored(text="-e/-d", color="red"),
                          "\"string\"")

            elif args.bin2hex:
                if args.help:
                    print(binNhex("0").help())
                elif args.encode or args.decode:
                    print("blizzardwrap --bin2hex", termcolor.colored(text="(no use of -e/-d)", color="red"),
                          "\"binary number\"")
                else:
                    if args.string:
                        print(binNhex(args.string).bin2hex())

                    else:
                        print("blizzardwrap --bin2hex \"" + termcolor.colored(text="string", color="red") +
                              "\"")


            elif args.hex2bin:
                if args.help:
                    print(binNhex("0").help())
                elif args.encode or args.decode:
                    print("blizzardwrap --hex2bin", termcolor.colored(text="(no use of -e/-d)", color="red"),
                          "\"hex string\"")
                else:
                    if args.string:
                        print(binNhex(args.string).hex2bin())

                    else:
                        print("blizzardwrap --hex2bin \"" + termcolor.colored(text="string", color="red") +
                              "\"")


            else:
                pass


        if args.url and len(sys.argv)>2:

            
            if args.url==1 and args.help or args.help and args.url=='f':                
                print(urlShredder("0", "0").help())


            elif args.decode:
                if args.string:
                    print(urlShredder(args.string, "0").decode())
                else:
                    print("blizzardwrap --url --decode/-d \"" + termcolor.colored(text="string", color="red") +
                              "\"")

            elif args.url=="f" and args.url!=1:
                if args.encode:
                    if args.string:
                        print(urlShredder(args.string, "f").encode())
                    else:
                        print("blizzardwrap --url f --encode/-e \"" + termcolor.colored(text="string", color="red") +
                                  "\"")
                else:
                    print("blizzardwrap --url f "+termcolor.colored(text="-e", color="red") +" "+ "\"string\"")

            elif args.url=="h" and args.help==False or args.url==1 and args.help==False:
                if args.encode:
                    if args.string:
                        print(urlShredder(args.string, "h").encode())
                    else:

                        print("blizzardwrap --url h --encode/-e \"" + termcolor.colored(text="string", color="red") +
                                  "\"")
                else:
                    print("blizzardwrap --url h "+termcolor.colored(text="-e", color="red") + " "+"\"string\"")

            else:
              if args.help==False:
                print("blizzardwrap --url", termcolor.colored(text="f/h -e", color="red"),
                      "\"string\"")
                print("blizzardwrap --url", termcolor.colored(text="-d", color="red"),
                      "\"string\"")
                print("blizzardwrap --url", termcolor.colored(text="-h", color="red"),
                      " (for more help)")
                
              else:
                pass

        else:
          print(mHelp().help())



    else:
        parser.print_help()



except:
    print(termcolor.colored(text="There is an error in your command", color="red"))
    print("blizzardwrap.py -h/--help [argument]          ", termcolor.colored(text="(for more help)", color="blue"))


