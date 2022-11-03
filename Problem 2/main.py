def check(my_string):
	brackets = ['()', '{}', '[]']
	while any(x in my_string for x in brackets):
		for br in brackets:
			my_string = my_string.replace(br, '')
	return not my_string

# Test Case: 1
string = "()[]{}"
print(string, "-", "true" if check(string) else "false")

# Test Case: 2
string = "([)]"
print(string, "-", "true" if check(string) else "false")

# Test Case: 3
string = "{{[](}})"
print(string, "-", "true" if check(string) else "false")

# Test Case: 4
string = "{[()]}"
print(string, "-", "true" if check(string) else "false")

