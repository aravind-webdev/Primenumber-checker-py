#using for loop
#no=5
no=int(input("Enter number:"))
flag=True

if no>2:
    for i in range(2,no):
        if (no%i) ==0:
            flag=False
            break

if flag:
     print(no,"is Prime number")
else:
     print(no, "is not Prime number")
