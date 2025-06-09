m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  #         0.    1.    2.     3.    4.     5.     6
days1 = sum(days[1:m1]) + d1
days2 = sum(days[1:m2]) + d2

diff = days2 - days1
diff = diff % 7

print(week[diff])
    
