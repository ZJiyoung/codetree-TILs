m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
day = d1
month = m1

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
week_index = 0
count = 0

while True:
    if week[week_index] == A:
        count += 1

    if day == d2 and month == m2:
        break
    
    day += 1
    week_index = (week_index + 1) % 7

    if day > days[month]:
        month += 1
        day = 1

print(count)
