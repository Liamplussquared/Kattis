temp = 0
for i in range(int(input())):
    period = input().split()
    x,y = float(period[0]), float(period[1])
    temp += x * y
print(str(round(temp,3)))

