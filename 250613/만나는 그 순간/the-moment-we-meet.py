n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
'''
L - / 0 / R + 
t[]와 t2[] 내 요소 총합은 동일 
'''

location = []
for i in range(n):
    if d[i] == "L":
        location += [-1] * t[i]
    else:
        location += [1] * t[i]

location2 = []
for j in range(m):
    if d2[j] == "L":
        location2 += [-1] * t2[j]
    else:
        location2 += [1] * t2[j]

now = 0
now2 = 0
result = -1
# 비교 
for i in range(len(location)):
    now += location[i]
    now2 += location2[i]

    if now == now2:
        result = i + 1
        break

print(result)
