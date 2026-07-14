n = int(input("enter a number : ")) 
t = n
s = 0
while t > 0:
    dig = t % 10
    f = 1
    for i in range(1, dig + 1):
        f *= i
    s += f 
    t //= 10
if s == n :
    print("it is strong number")
else:
    print("it is not a strong number")

