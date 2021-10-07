


from difflib import Differ

with open('sort_code.py') as file_1, open('damnit.py') as file_2:
	differ = Differ()

	for line in differ.compare(file_1.readlines(), file_2.readlines()):
		print(line)


