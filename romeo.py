## practice with romeo.txt file

print "begin!"
file = raw_input("Enter file name: ")
input = open(file)
for line in input:
	line = line.split()
	print line
newlist = []
print newlist
for word in line:
	newlist.append(word)
	print newlist
print "done"