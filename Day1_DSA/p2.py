n=int(input())

sum=0

while n!=0:
    last_digit=n%10
    sum+=last_digit
    n=int(n/10)

print(sum)