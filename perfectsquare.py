#WAP TO CHECK WHETHER GIVEN NUMBER IS A PERFECT SQUARE NUMBER OR NOT
n = int(input("enter a number : "))
i = 1
while i * i <= n:
    if i * i == n:
        print("It is a Perfect Square")
        break
    i += 1
else:
    print("It is not a Perfect Square")
    