import subprocess
import re

subprocess.call(["clear"])

f = open("banner.txt","r")
print(f.read())
f.close()

interface = input("[+] Interface You Want To Change Its Mac > ")

if interface:

	ifconfig = subprocess.run(["ip","link","show"], stdout=subprocess.PIPE)
	text = ifconfig.stdout.decode("UTF-8")
	result = text.find(": " + interface + ":")

	if (result != -1):
		ifconfig_output = subprocess.check_output(["ifconfig", interface])
		current_mac = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_output))
	
		if current_mac:
			print("[+] Your Current Mac Address is " + current_mac.group(0))
		else:
			import sys
			print("[-] This Interface Has No Mac Address")
			sys.exit(1)

		new_mac = input("[+] New Mac Address > ")
		
		if new_mac:

			if re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(new_mac)) and len(new_mac) == 17:
			
				print("[+] Changing Mac Address To " + new_mac)

				subprocess.call(["ifconfig", interface, "down"])
				subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
				subprocess.call(["ifconfig", interface, "up"])

				ifconfig_output = subprocess.check_output(["ifconfig", interface])
				current_mac = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_output))

				if new_mac == current_mac.group(0):
					print("[+] Your New Mac Address For " + interface + " Is " + new_mac)
				else:	
					print("[-] Failed To Change Mac Address")
				
			else:
				print("[-] Invalid Mac Address")

		else:
			print("[-] Please Enter a New Mac")
	else:
		print("[-] Invalid Interface")
else:
	print("[-] Please Enter Your Interface")


