n=int(input())

arr=list(map(int,input().split()))

def twoSum(arr,target):
    hashMap=dict()
    for i in range(len(arr)):
        if arr[i] in hashMap:
            return [hashMap[arr[i]],i]
        hashMap[target-arr[i]]=i
    return [-1,-1]

print(twoSum(arr,7))