name = input("What is your name? ")
if name.isalpha():
	pass
else:
	print("Your name is incorrect. Please enter your name correct" )
surname = input("What is your surname? ")
if surname.isalpha():
	print("Hello, Dear", name, surname, "my sait is welcome to you")
else:
	print("Your surname is incorrect. Please enter your surname correct")
age = input("How old are you? ")
if age.isdigit():
	if int(age) > 0:
		pass
else:
	print("Your age is incorrect. Please enter your age correct")
mail = input("Enter your mail. ")
if "@" in mail and "." in mail:
	pass
else:
	print("Your mail is incorrect. Please enter your mail correct")
password = input("Enter your password.In password must be [a-z], [A-Z] and [0-9] and 8 characters     ")
if len(password) >= 8 and len(password) <= 12 and password.isalnum():
	print("print")
