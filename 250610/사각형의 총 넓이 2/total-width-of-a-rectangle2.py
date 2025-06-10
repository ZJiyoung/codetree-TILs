n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

'''
겹치는 넓이는 한 번만 세야 함
2차원 배열 

'''
sheet = [[0] * 201 for _ in range(201)]
count = 0

for t in range(n):
    for i in range(x1[t]+100,x2[t]+100):
        for j in range(y1[t]+100,y2[t]+100):
            sheet[i][j] = 1

'''
2차원 배열 sheet 검색ㅎ 0이 아닌 1인 부분들 넓이 구하면 됨. 
아 그럼 개수를 구하면 되네 
'''

for i in range(len(sheet)):
    for j in range(len(sheet[i])):
        if sheet[i][j] != 0:
            count += 1

print(count)