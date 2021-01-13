


print("\n"*100)
print("         Hello!  \n")
print("         Welcome to my interactive python shell. This is a simple shell where you can execute your own small pieces of python code!  \n")
print("         Feel free to play around with the program, but be AWARE cause it could crash at anytime!!!  \n")
print("         NOTE: You can stop the program by running either 'stop', or 'exit' at anytime.   \n")
print("         Have Fun! \n")
print("      -Shrey Patel :)")
print("\n"*3)


# CONSTANTS
EXIT_STRING = 'STOP,EXIT,stop,exit,Stop,Exit'
EMPTY_STRING = ' ' * 10000
while True: 


	usr_input = input("INPUT : " )

	if usr_input in EMPTY_STRING: 
		print("Please enter a command!")
		continue

	

	if usr_input in EXIT_STRING: 
		print("\n" * 100)
		break 

	try:
		value = eval(usr_input)
		print("OUTPUT : ",value)
	except: 
		try: 
			exec(usr_input)	
		except Exception as error: 
			print("ERROR: ", error)




print("Thank-you for trying out my interactive python shell! I hope you enjoyed it!! - Shrey")
print("\n" * 2)
