#https://open.kattis.com/problems/sodasurpler
s = [int(x) for x in input().split()]
bottles = s[0] + s[1]
total = int(0)
while bottles >= s[2]:
    bottles -= s[2]
    total += 1
    bottles+=1
print(total)