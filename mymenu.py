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
		1: Basic Linux Commands
		3: AWS
		4: Hadoop
		5: Docker
		6: configure web server
		7: Exit
			""")
while True:
	
		main_menu()
		user_input = int(input("Enter your choice."))
		if user_input==1:
			linux();
		"""elif user_input==2:
			
		elif user_input==3:
			aws()
		elif user_input==4:
			hadoop()
		elif user_input==5:
			docker()
		elif user_input==6:
			webserver()"""
		elif user_input==7:
			break
		else:
			os.system("tput setaf 3")
			print("\t\t\tinvalid choice")
			os.system("tput setaf 7")
