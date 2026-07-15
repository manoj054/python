n = int(input("enter a number : "))
sum = 0
digits = len(str(n))
t = n
while t > 0:
    digit = t % 10
    sum = sum + (digit ** digits)
    t = t // 10
print(sum)
if sum == n :
    print("it is a armstrong number ")
else:
    print("it is not a armstrong number ")