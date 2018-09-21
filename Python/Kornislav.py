#https://open.kattis.com/problems/kornislav
n = input().split()
m = sorted(int(i) for i in n)
print(m[0]*m[2])