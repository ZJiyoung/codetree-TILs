n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

ksum = 0
kmax = 0

for i in range(n-k): 
    ksum = 0

    for j in range(k):
        ksum += arr[i + j]

    if ksum > kmax : 
        kmax = ksum 

print(kmax)