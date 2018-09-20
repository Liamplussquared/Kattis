#https://open.kattis.com/problems/rijeci
n = int(input())
A = 1
B = 0
while n:
    newA = 0
    newB = 0

    newA = B
    newB = A+B

    A = newA
    B = newB
    n-=1
print(str(A)+" "+str(B))