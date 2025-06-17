n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
score = 0 
max_score = 0

for i in range(n):
    for j in range(i,n):
        if (x[j]-x[i]) == k:

            score = 0

            for t in range(i, j+1):
                if c[t] == 'G':
                    score += 1
                elif c[t] == 'H':
                    score += 2

            if score > max_score:
                max_score = score

print(max_score)

