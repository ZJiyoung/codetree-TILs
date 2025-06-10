n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

'''
총 n개의 칸 

k번의 명령 예정
튜플로 주어진 (a,b) a~b 범위에 해당하는 칸수에 count += 1

n개의 칸을 전부 돌면서 각각 count 중 가장 큰 값 출력 
'''

count = [0]*n

for command in commands:
    for i in range(command[0],command[1]+1,1):
        count[i-1] += 1

max = 0
for i in range(n):
    if max < count[i]:
        max = count[i]

print(max)

