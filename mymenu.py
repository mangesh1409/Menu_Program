import os;
import getpass;

password=getpass.getpass("Enter your password : ");

if password!='123':
	os.system("tput setaf 1");
	print("Wrong Password");
	os.system("tput setaf 7");	
	exit();

"""print("Where you want to run this menu ? ");
print("Press 1 : Local");
print("Press 2 : Remote");
loc=int(input("Eneter your choice : "));"""


def main_menu():
 print("\t\t\t---------------------");
 os.system("tput setaf 3");
 print("\t\t\tWelcome To Main Menu !!");
 os.system("tput setaf 7");
 print("\t\t\t---------------------");
 print("""
	1: Basic Linux Commands
	2: Docker
	3: AWS
	4: Hadoop	
	6: configure web server
	7: Exit
	""")

def linux():
	os.system("tput setaf 2")
	print("********************************************************************************")
	os.system("tput setaf 3")
	print("\t\t\tWELCOME TO Linux OS")
	os.system("tput setaf 2")
	print("********************************************************************************")
	os.system("tput setaf 7")
	login=input("you want to login local/remote :-")
	
	while True:
		#os.system("clear");
		if login=="local":
			print("""********************************************************************************
			Select Option
			1. See Date
			2. See Calendor
			3. Show Partition
			4. Show System Info
			5. Show Memory Status
			6. Show All Mounted Devices
			7. Show IP Address
			8. Go To Main Menu
			*************************************************************************************""")
			input_user=input("Enter your choice:-")
			if int(input_user)==1:
				os.system("date")
			elif int(input_user)==2:
				os.system("cal")
			elif int(input_user)==3:
				os.system("fdisk -l")
			elif int(input_user)==4:
				os.system("lscpu")
			elif int(input_user)==5:
				os.system("free -m");
			elif int(input_user)==6:
				os.system("df -h")
			elif int(input_user)==7:
				os.system("ifconfig")
			elif int(input_user)==8:
				return;
			else:
				os.system("tput setaf 1")
				print("\t\t\tinvalid choice")
				os.system("tput setaf 7")
			#os.system("clear");
                      

def docker():

	os.system("tput setaf 2")
	print("********************************************************************************")
	os.system("tput setaf 3")
	print("\t\t\tWELCOME TO Docker Menu")
	os.system("tput setaf 2")
	print("********************************************************************************")
	os.system("tput setaf 7")
	login=input("you want to login local/remote:-")
	
	while True:
		if login=="local":
			print("""
			1. See Date
			2. See Calendor
			3. Show Partition
			4. Show System Info
			5. Show Memory Status
			6. Show All Mounted Devices
			7. Show IP Address
			8. Go To Main Menu
			""")
			input_user=input("Enter your choice:-")
			if int(input_user)==1:
				os.system("date")
			elif int(input_user)==2:
				os.system("cal")
			elif int(input_user)==3:
				os.system("fdisk -l")
			elif int(input_user)==4:
				os.system("lscpu")
			elif int(input_user)==5:
				os.system("free -m");
			elif int(input_user)==6:
				os.system("df -h")
			elif int(input_user)==7:
				os.system("ifconfig")
			elif int(input_user)==8:
				return;
			else:
				os.system("tput setaf 3")
				print("\t\t\tinvalid choice")
				os.system("tput setaf 7")





while True:

	os.system("clear") 
	main_menu()
	user_input = int(input("Enter your choice : "))
	
	if user_input==1:
		linux();
	if user_input==2:
		docker();
	elif user_input==7:
		break
	else:
		os.system("tput setaf 3")
		print("\t\t\tinvalid choice")
		os.system("tput setaf 7")





