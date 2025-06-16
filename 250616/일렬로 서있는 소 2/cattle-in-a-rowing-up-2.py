N = int(input())
A = list(map(int, input().split()))

# Please write your code here.
'''
A 리스트의 인덱스 i-1 j-1 k-1
A[i] <= A[j] and A[j] <= A[k]

3개 골라 
크기 비교 
-> 조합 Combination

5
3 1 7 10 4

3 7 10
1 7 10
'''
A.insert(0, 1) #배열A 인덱스 0번에 요소 1 추가 

arr = []
count = 0

for i in range(1, N-1): #1 ~ i
    for j in range(i+1, N): #i+1 ~ 
        for k in range(j+1, N+1): #j+1 ~ n
            if A[i] <= A[j] and A[j] <= A[k]:
                # for x in [i, j, k]:
                #     if x not in arr:
                #         arr.append(x)
                # # print(*arr)
                count += 1

print(count)
