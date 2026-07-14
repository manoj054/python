m = int(input("Enter first number: "))
n = int(input("Enter second number: "))
product = 1
for i in range(m, n + 1):
    if i % 2 != 0:
        product *= i
print(product)