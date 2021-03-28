#!/usr/bin/env python3




import os
import pkg_resources
#import colorama
#import termcolor
import platform
from distutils.dir_util import copy_tree

#colorama.init()

getPackages = pkg_resources.working_set
getPackagesList = sorted(["{:s}=={:s}".format(one.key, one.version) for one in getPackages])
notInstalled = []

for each in getPackagesList:
    if "colorama" in each:
        notInstalled.append(each)
    elif "termcolor" in each:
        notInstalled.append(each)
    else:
        pass
if len(notInstalled) >= 1:

    try:
        print("[Warning]:\nFollowing libraries not installed: " if len(
                notInstalled) > 1 else "[Warning:]\nFollowing library not installed: ")
        print("blizzardwrap wants to install these libraries " + " ".join(notInstalled) if len(
            notInstalled) > 1 else "blizzardwrap wants to install this library " + " ".join(notInstalled))
        whatToDo = input("Install or not? Y or N: ")[:3].upper()
        if whatToDo == "YES" or whatToDo == "Y":

            if "LINUX" in platform.platform().upper().split("-"):
                os.system("python3 -m pip install " + " ".join(notInstalled))

            elif "WINDOWS" in platform.platform().upper().split("-"):                
                os.system("python -m pip install " + " ".join(notInstalled))
            
            else:
                try:
                    os.system("python -m pip install " + " ".join(notInstalled))
                except:
                    os.system("pthon3 -m pip install " + " ".join(notInstalled))


        elif whatToDo == "NO" or whatToDo == "N":
            print("Manually download " + " ".join(notInstalled))
        else:
            print("Invalid input...try again!")
    except:
        print("Could'nt be installed...Please manually install them")
else:
    print("Everything is all set up!")


'''
try:
	if "LINUX" in platform.platform().upper().split("-"):
		print("Would you like to copy blizzardwrap to environment path")
		print("By doing so you can simply type blizzardwrap and use it")
		doIt=input("("+str(termcolor.colored(text="Y", color="green"))+" or "+str(termcolor.colored(text="N", color="red"))+"): ")[:3].upper()
		if doIt=="Y" or doIt=="YES":

			copy_tree(src="../blizzardwrap/", dst="/usr/bin/blizzardwrap/")			
			print(str(termcolor.colored(text="Successfully done!", color="blue")))
			print("Now just type blizzardwrap -h")
		else:
			print(termcolor.colored(text="Operation terminated!!", color="red"))
	else:
		pass

except:
	print(str(termcolor.colored(text="Error occured",color="red")))
	print(str(termcolor.colored(text="Run with sudo", color="green")))
'''
