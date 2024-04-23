def printRepeatingDigits(n):
    buc=[0 for i in range(10)]
    while n!=0:
        last_digit=n%10
        buc[last_digit]+=1
        n=int(n/10)
    for i in range(10):
        if buc[i]>1:
            print(i,end=" ")

n=int(input())

printRepeatingDigits(n)