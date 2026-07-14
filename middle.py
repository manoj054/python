a = input("Enter a number: ")

length = len(a)

if length % 2 == 0:
    mid = length // 2
    print("Middle digits:", a[mid - 1:mid + 1])
else:
    mid = length // 2
    print("Middle digit:", a[mid])
    