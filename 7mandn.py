n = int(input("enter a number : "))
m = int(input("enter a number : "))
count = 0
for i in range(n, m+1):
    if i % 7 == 0:
        count += 1
print(count)