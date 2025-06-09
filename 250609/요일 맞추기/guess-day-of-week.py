m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

'''
d1에서 7만큼 커질때마다 월요일 
m1월 d1일에서 m2월 d2일까지 일수를 구하고 
그 다음에 7로 나눠서 나머지를 구하고 그 나머지에 해당하는 요일이 정답 
'''

days1 = sum(days[1:m1]) + d1
days2 = sum(days[1:m2]) + d2

diff = abs(days1 - days2)

if (days1 - days2) >= 0 :
    print(week[7-diff])
else:
    print(week[diff])
    
