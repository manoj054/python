n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers.sort()

print("Ascending Order:", numbers)