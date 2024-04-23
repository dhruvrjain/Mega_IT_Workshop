n=int(input())

first,second=-1,1

for i in range(n):
    third=first+second
    first=second
    second=third
    print(third,end=" ")

# n=5
# 0, 1, 1, 2, 3