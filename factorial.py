number=int(input("please enter a number: "))
factorial=1
if number<0:
    print("sorry, factorial does not exist for negative numbers")
elif number==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("the factorial of",number,"is",factorial)
