n = int(input())

# Please write your code here.

result = []

while True:
    if n < 2:
        result.append(n)
        break
    
    result.append(n % 2)
    n //= 2 

# result = result[::-1]
# print(*result)

for i in result[::-1]:
    print(i,end="")