n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
people = sorted([(x[i], c[i]) for i in range(n)])

max_score = 0

for i in range(n):
    score = 0
    for j in range(i, n):
        if people[j][0] - people[i][0] <= k:
            if people[j][1] == 'G':
                score += 1
            elif people[j][1] == 'H':
                score += 2
        else:
            break
    max_score = max(max_score, score)

print(max_score)

