n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
count = 0

for i in range(n):
    for j in range(i, n):
        test_sum = 0
        for t in range(i,j+1):
            test_sum += arr[t]
            length = j-i+1
        if test_sum % length == 0:
            if (test_sum // length) in arr[i:j+1]:
                count += 1
print(count)