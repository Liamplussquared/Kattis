#https://open.kattis.com/problems/boatparts
parameters = input().split()
parts = int(parameters[0])
c = set()
f = 1
for i in range(int(parameters[1])):
    p = input()
    if p not in c:
        c.add(p)
        if len(c) == parts:
            print(i+1)
            f = 0
            break
if f: print("paradox avoided")

