n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
'''
0 1 2 3 4
1 2 3 2 6
'''
distance = 0
min = 100000

for i in range(n):
    distance = 0

    for j in range(n):
        distance += A[j] * abs(i-j) 
    
    if distance < min:
        min = distance 
    

print(min)