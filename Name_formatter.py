def format_name(first_name, last_name):
	if (first_name =="" and last_name == ""):
		string = ""
	elif first_name =="":
		string = "Name: " + last_name
	elif last_name =="":
		string = "Name: " + first_name
	else:
		string = "Name: " + last_name + ", " + first_name
	return string 

print(format_name("Ernest", "Hemingway"))
# Returns the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Returns the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Returns the string "Name: Voltaire"

print(format_name("", ""))
# Returns an empty string
