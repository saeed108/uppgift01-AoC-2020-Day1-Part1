# Read in the input file
with open('inmatning01.txt') as x:
    lines = x.readlines()

#Creating a variable, convert list of str to list of intand removes any leading and trailing
numbers =  [int(line.strip()) for line in lines]
larg = -1

#Creating LOOPS (for) and Conditions
for i in range(len(numbers)-1):
    for l in range(i+1, len(numbers)):
        number1 = numbers[i]
        number2 = numbers[l]
        
# Count the increases and print the answer
        if number1+number2 ==2020:
            equipoise = number1 * number2
       
            if  equipoise > larg:
             larg =  equipoise

#Print the resualt
print(larg)
