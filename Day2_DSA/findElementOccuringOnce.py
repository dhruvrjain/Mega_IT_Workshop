n=int(input())

arr=list(map(int,input().split()))

def findElement(arr,n):
    low=0
    upp=n-1

    while(low<=upp):
        if(low==upp):
            return arr[low]
        mid=int((low+upp)/2)
        if(mid>0 and arr[mid]==arr[mid-1]):
            if((mid-low)%2):
                low=mid+1
            else:
                upp=mid-2
        elif mid<n-1 and arr[mid]==arr[mid+1]:
            if (upp-mid)%2:
                upp=mid-1
            else:
                low=mid+2
        else:
            return arr[mid]
        
print(findElement(arr,n))