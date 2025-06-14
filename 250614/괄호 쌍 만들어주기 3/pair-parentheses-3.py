A = input()

# Please write your code here.
'''
) 부터 나오면 무시 
( 나오는 순간 시작 

( 1개 당 ->  뒤에 나오는 ) 개수 count
'''

A = list(A)
count = 0

for i in range(len(A)):
    if A[i] == '(':
        start_index = i 
        break

for i in range(start_index,len(A)):
    if A[i] == '(':
        for j in range(i+1,len(A)):
            if A[j] == ')':
                count += 1
    
print(count)
