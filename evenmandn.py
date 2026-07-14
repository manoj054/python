m = int(input("Enter first number: "))
n = int(input("Enter second number: "))
sum = 0
for i in range(m, n + 1):
    if i % 2 == 0:
        sum += i
print(sum)