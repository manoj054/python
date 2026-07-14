b = int (input("enter a number : "))
c = int (input("enter a number : "))
a = int (input("enter a number : "))
if a>b and a>c :
    print("a is big one")
elif b>a and b>c:
    print("b is big one")
elif c>a and c>b:
    print("c is big one")
else:
    print("equal number")