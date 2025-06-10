binary = input()

# Please write your code here.

binary = list(binary)

result = int(binary[0])

for i in binary[1:]:
    result *= 2 
    result += int(i)

print(result)
