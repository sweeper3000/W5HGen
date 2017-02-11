print("W5HGen 3.0")
print("")

mode = input("File mode (1) or console output (2)? -> ")

def initFileOutput():
	print("Let's begin constructing the 5 points as well as the header. Put in information at the prompts")
	projectName = input("Name of your project. This will be saved as 'w5h-projectName.txt' where projectName is the name you specify -> ")

	projectTitle = input("What should the header of the file be? The title will be converted to all caps -> ")
	who = input("Who? Names of people relevent to the project -> ")
	what = input("What happened? -> ")
	when = input("When did the event happen? -> ")
	where = input("Where did the event happen? -> ")
	why = input("Why did it happen? -> ")
	how = input("How did it happen? -> ")

	w5hCreate = open("w5h-" + projectName + ".txt", "w")
	w5hCreate.write(projectTitle.upper() + "\n \n")
	w5hCreate.write("WHO: " + who + "\n")
	w5hCreate.write("WHAT: " + what + "\n")
	w5hCreate.write("WHEN: " + when + "\n")
	w5hCreate.write("WHERE: " + where + "\n")
	w5hCreate.write("WHY: " + why + "\n")
	w5hCreate.write("HOW: " + how + "\n")
	w5hCreate.close()
	
	print("")
	print("Your file is saved. Here's what it looks like:")
	w5hRead = open("w5h-" + projectName + ".txt", "r")
	print("NOTE: The beginning and end headers are not included in the text file.")
	print("-----BEGIN W5H TEXT----- \n")
	print(w5hRead.read())
	print("----END W5H TEXT-----")
	w5hRead.close()
	return;

def initConsoleOutput():
	print("Let's begin constructing the 5 points as well as the header. Put in information at the prompts")

	projectTitle = input("What should the header of the file be? The title will be converted to all caps -> ")
	who = input("Who? Names of people relevent to the project -> ")
	what = input("What happened? -> ")
	when = input("When did the event happen? -> ")
	where = input("Where did the event happen? -> ")
	why = input("Why did it happen? -> ")
	how = input("How did it happen? -> ")

	print("Here's the output: \n")
	print(projectTitle.upper() + "\n")
	print("WHO: " + who)
	print("WHAT: " + what)
	print("WHEN: " + when)
	print("WHERE: " + where)
	print("WHY: " + why)
	print("HOW: " + how)
	return;

if (mode == "1"):
        initFileOutput()
elif (mode == "2"):
        initConsoleOutput()
else:
        print("Invalid input")
