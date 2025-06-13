N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

count = 1
countb = 1
result = 0

for i in range(N-1):
    if arr[i] > 0 and arr[i+1] > 0:
        count += 1
        result = max(result, count)
    elif arr[i] < 0 and arr[i+1] < 0:
        countb += 1
        result = max(result, countb)
    else: 
        count = 1
        countb = 1

print(result)