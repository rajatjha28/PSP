import sys
import re

print(type(sys.argv))

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

def check(Ip):
	if(re.search(regex,Ip)):
		return True;
	else:
		return False;

# print ("Enter the IP address:")
ipa = sys.argv
# while(True):
# 	if(check(ipa)):
# 		break;
# 	else:
# 		print ("Kindly enter correct IP address:")
# 		ipa=input()

print (ipa)

# print ("Enter the starting and ending port:")