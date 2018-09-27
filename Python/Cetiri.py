#https://open.kattis.com/problems/cetiri
s = [int(i) for i in input().split()]
#a = list(map(int, input().split()))
s.sort()
d1 = abs(s[1]-s[0])
d2 = abs(s[2]-s[1])
d = min(d1,d2)

if abs(s[1]-s[0]) != d:
  print(s[0]+d)
elif abs(s[2]-s[1]) != d:
  print(s[1]+d)
else: print(s[2] + d)