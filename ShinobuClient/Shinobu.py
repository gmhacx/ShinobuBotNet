import requests
import os
import sys
import time
from colorama import Fore, Back, init
init(autoreset=True)
def clear():
    os.system('clear')
logo = Fore.MAGENTA + '''
░██████╗██╗░░██╗██╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░░█████╗░████████╗███╗░░██╗███████╗████████╗
██╔════╝██║░░██║██║████╗░██║██╔══██╗██╔══██╗██║░░░██║██╔══██╗██╔══██╗╚══██╔══╝████╗░██║██╔════╝╚══██╔══╝
╚█████╗░███████║██║██╔██╗██║██║░░██║██████╦╝██║░░░██║██████╦╝██║░░██║░░░██║░░░██╔██╗██║█████╗░░░░░██║░░░
░╚═══██╗██╔══██║██║██║╚████║██║░░██║██╔══██╗██║░░░██║██╔══██╗██║░░██║░░░██║░░░██║╚████║██╔══╝░░░░░██║░░░
██████╔╝██║░░██║██║██║░╚███║╚█████╔╝██████╦╝╚██████╔╝██████╦╝╚█████╔╝░░░██║░░░██║░╚███║███████╗░░░██║░░░
╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═════╝░░╚═════╝░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚══╝╚══════╝░░░╚═╝░░░
'''
clear()
print(logo)

if(os.path.isfile('URL.txt') == False):
	#installion
	installion = input(Fore.YELLOW + 'Start installing the panel? (y/n): ')
	#USER AGREEMENT
	if (installion == "y"):
		print('USER AGREEMENT: ')
		print("I, the creator and all those associated with the development and production of this program are not responsible for any actions and or damages caused by this software. You bear the full responsibility of your actions and acknowledge that this software was created for educational purposes only. This software s intended purpose is NOT to be used maliciously, or on any system that you do not have own or have explicit permission to operate and use this program on. By using this software, you automatically agree to the above.")
		a = input(Fore.YELLOW + 'Do you accept this agreement? (y/n): ')
		if (a == 'y'):
			clear()
			URL = input(Fore.YELLOW + '[?] - Enter URL: ')
			print(requests.get(URL + 'install.php?ans=Yes'))
			print(Fore.GREEN + 'Installed')
			time.sleep(1)
			clear()
			#connect
			file = open('URL.txt', 'w')
			file.write(URL)
			file.close()
			print(Fore.GREEN + '[!] - url ' + URL + ' set')
			exit()
		else:
			exit()
	else:
    	#connect
		URL = input(Fore.YELLOW + '[?] - Enter URL: ')
		file = open('URL.txt', 'w')
		file.write(URL)
		file.close()
		print(Fore.GREEN + '[!] - url ' + URL + ' set')
		exit()

else:
	print(Fore.GREEN + '[!] - Get URL')
	file = open('URL.txt')
	url = file.read()
	print(Fore.GREEN + '[!] - URL set ' + url)
	password = input(Fore.YELLOW + 'Enter your password: ')
	userslist = requests.get(url + 'getusers.php?password=' + password)
	clear()
	print(logo)
	print(userslist)
