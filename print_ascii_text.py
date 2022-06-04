import sys
file = open("ascii_alphabet.txt")


print("Enter your input: ")
string = input()
string = string.upper()
char_arr = []
num_arr = []


for idx in string:
	char_arr.append(idx)
print(char_arr)

original_stdout = sys.stdout

with open("output.txt", "w") as outfile:
	sys.stdout = outfile
	
	for idx in char_arr:
		num_idx = (ord(idx)-32)*7
		num_arr.append(num_idx)
	#print(num_arr)
	#print("\nPRINTING\n")
	line = file.read().splitlines()
	for layer in range(7):
		for idx in num_arr:
			print(line[idx], end=" ")
		num_arr = [x+1 for x in num_arr]
		print()
file.close
outfile.close
sys.stdout = original_stdout