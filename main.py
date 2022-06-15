import string, random
password = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
inputfile = False; answered = False
while not answered:
	tofile = input("to file (y/n)?")
	if tofile == "y":
		inputfile = True; answered = True
	elif tofile == "n":
		inputfile = False; answered = True
	else:
		print("y or n")
if inputfile:
	with open("password.txt", "w+") as f:
		f.write(password)
		
text = f"Password is {password} and written to password.txt" if inputfile else f"Password is {password}"
print(text)	
