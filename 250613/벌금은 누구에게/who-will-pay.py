N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
'''
1 2 3 4 ... N 학생번호 
벌금 기준은 K번 

M번 (학생번호) > student[]
2
2
4
2
2
5
6
> 2번이 벌금 

student[] 읽어서 순서대로 검색했을 때 같은 학생번호가 총 K번 이상 나오는 순간 그 학생번호 출력 

'''

count = [0] * (N+1)
result = -1

for i in range(M):
    count[student[i]] += 1
    if count[student[i]] == K:
        result = student[i]

print(result)