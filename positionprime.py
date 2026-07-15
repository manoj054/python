n = int(input("enter a number position : "))
num = 2
count = 0 
while True:
    prime =  True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        count += 1
        if count == n:
            print("Prime number =", num)
            break
    num += 1