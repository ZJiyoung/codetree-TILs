n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
'''
6 3
1 1 1 9 9 9

정답 27 
나 19
'''

ksum = 0
kmax = 0

for i in range(n-k + 1): # 6 - 3 + 1
    ksum = 0

    for j in range(k): # 0 1 2 
        ksum += arr[i + j]

    if ksum > kmax : 
        kmax = ksum 

print(kmax)