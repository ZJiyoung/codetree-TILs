n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
'''
x 최댓값 - x 최솟값 
* 
y 최댓값 - y 최솟값
'''

xlength = max(x) - min(x)
ylength = max(y) - min(y)
min_extent = xlength * ylength 

for i in range(n): #0~n-1

    if x[i] == max(x) or x[i] == min(x) or y[i] == max(y) or y[i] == min(y):
        # del x[i]
        # del y[i]
        new_x = [k for idx, k in enumerate(x) if idx != i]
        new_y = [k for idx, k in enumerate(y) if idx != i]

        #다시 max랑 min 구하기
        xlength = max(new_x) - min(new_x)
        ylength = max(new_y) - min(new_y)

    extent = xlength * ylength 
    
    if min_extent > extent:
        min_extent = extent

print(min_extent)

    

