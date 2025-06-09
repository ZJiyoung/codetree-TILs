a, b, c = map(int, input().split())

# Please write your code here.

day = 11
hour = 11
minute = 11

if (a, b, c) < (day, hour, minute):
    print(-1)
else: 
    elapsed_time = 0 

    while True: 
        if day == a and hour == b and minute == c:
            break

        minute += 1
        elapsed_time += 1

        if minute > 59:
            hour += 1
            minute = 0
        
        if hour > 23:
            day += 1
            hour = 0

        # minute += 1
        # elapsed_time += 1
    
    print(elapsed_time)
