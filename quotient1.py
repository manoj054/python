a = int(input("enter a number : "))
b = int(input("enter a number : "))
count = 0
while a >= b:
    a = a - b
    count = count+1
print(count)