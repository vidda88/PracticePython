pics_category = {}

with open('Training_01.txt') as open_file:
	line = open_file.readline()
	while line:
		line = line[3:-26]
		if line in pics_category:
			pics_category[line] += 1
		else:
			pics_category[line] = 1
		line = open_file.readline()

print(pics_category)