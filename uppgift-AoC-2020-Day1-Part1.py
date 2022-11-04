# Read in the input file
file = open('inmatning01.txt')
test_inmatning = file.read()
file.close()

# Split the input into separate lines
test_inmatning = test_inmatning.splitlines()

# Convert list of str to list of int
data = []
for elem in test_inmatning:
    data.append(int(elem))

# Count the increases and print the answer
result = 0
for idx in range(1, len(data)):
    if data[idx] > data[idx-1]:
        result = result + 1
print(result) 