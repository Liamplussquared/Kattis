#https://open.kattis.com/problems/reversebinary
r = bin(int(input()))[2:][::-1]
print(int(r,2))