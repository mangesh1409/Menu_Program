import os
import getpass

print("\t\t\t---------------------");
os.system("tput setaf 3");
print("\t\t\tWelcome To My Menu !!");
os.system("tput setaf 7");
print("\t\t\t---------------------");

password=getpass.getpass("Enter your password : ");

if password!='123':
	os.system("tput setaf 1");
	print("Wrong Password");
	os.system("tput setaf 7");	
	exit();
print("Where you want to run this menu ? ");
print("Press 1 : Local");
print("Press 2 : Remote");
loc=int(input("Eneter your choice : "));


def main_menu():
	print("""
		1: Date
		2: calender
		3: AWS
		4: Hadoop
		5: Docker
		6: configure web server
		7: Exit
			""")

