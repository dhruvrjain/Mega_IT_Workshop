n=int(input())

arr=list(map(int,input().split()))

def search(arr,target):
    low=0
    upp=len(arr)-1

    while(low<=upp):
        mid=int((low+upp)/2)
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            upp=mid-1
    return -1

print(search(arr,7)) # 6
print(search(arr,11)) # -1