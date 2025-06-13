n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

count = 1
max = 0

for i in range(n-1):
    if arr[i] == arr[i+1]:
        count += 1
        if count > max:
            max = count
    else:
        count = 1

print(max)
