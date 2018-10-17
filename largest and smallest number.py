lst = []
number1 = (input("Please enter the 10 numbers"))
for n in range(10):
    number2 = int(input("Please enter the number: "))
    lst.append(number2)
print("Largest number in the list is :", max(lst))
print("smallest number in the list is :", min(lst))
