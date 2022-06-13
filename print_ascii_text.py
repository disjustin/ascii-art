import sys
file = open("ascii_alphabet.txt")

#print ('Number of arguments:', len(sys.argv))
#print ('Argument List:', str(sys.argv))

# input handling
if len(sys.argv) > 2:
	string = " ".join(sys.argv[1:])
elif len(sys.argv) == 2:
	list = sys.argv[1:]
	string = sys.argv[1]
	i = 2
	while i < len(list):
		string += ' ' + i
else:
	print ('Please enter your input:')
	string = input()
string = string.upper()
char_arr = []
num_arr = []
# print character string
for idx in string:
	char_arr.append(idx)
#print(char_arr)

for idx in char_arr:
	num_idx = (ord(idx)-32)*7
	num_arr.append(num_idx)
#print(num_arr)

# append to output.txt
original_stdout = sys.stdout
with open("output.txt", "a") as outfile:
	sys.stdout = outfile
	
	line = file.read().splitlines()
	for layer in range(7):
		for idx in num_arr:
			print(line[idx], end=" ")
		num_arr = [x+1 for x in num_arr]
		print()
file.close
outfile.close
sys.stdout = original_stdout