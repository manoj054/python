a = int(input("enter a number : "))
b = a
rev = 0
while a > 0:
    digit = a % 10 
    rev = (rev*10) + digit 
    a = a // 10
print(rev)
if rev ==  b:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
