## practice with romeo.txt file

try: input = raw_input
except NameError: pass

print('begin!')
print('Enter file name: ')
file = input()
input = open(file)
for line in input:
	line = line.split()
	print(line)
print('done!')
