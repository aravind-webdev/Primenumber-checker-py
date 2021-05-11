#using while-loop
no = int(input('Please enter a number:'))

i = 2
flag = True

while no>i:
    if no%i == 0:
        flag = False
        print ("Your number is NOT a prime number!");
    i = i + 1

if flag == True:
    print ("Your number is a prime number!");
