lst=[]
num= input("Please enter the 10 numbers")
for n in range(10):
    num2=int(input("Please enter the number:"))
    lst.append(num2)
    sum = 0
for n in range(0,n+1,1):
    sum=sum+num2
print("SUM of first 10 number is: ",sum)
average = 0
average = sum / 10
print("Average of first 10 number is: ",average)
