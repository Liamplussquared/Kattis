
def sum(i):
    s = str(i)
    r = 0
    for c in s:
        r += int(c)
    return r

l = int(input()) 
d = int(input())
x = int(input())
check = False

for i in range(l, d+1):
    if sum(i) == x:
        print(i)
        break

for i in range(d, l-1, -1):
    if sum(i) == x:
        print(i)
        break 

