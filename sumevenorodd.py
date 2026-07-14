a = int(input("enter a number : "))
sum = 0
while a > 0:
    dig = a % 10 
    sum = sum + dig
    a = a // 10
print(sum)
if sum % 2 == 0:
    print("sum is an even number")
else:
    print("sum is a odd number")