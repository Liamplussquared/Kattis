#https://open.kattis.com/problems/cetvrta
A = input().split()
B = input().split()
C = input().split()
x = [int(A[0]), int(B[0]), int(C[0])]
y = [int(A[1]), int(B[1]), int(C[1])]
point = []
for i in x:
    if x.count(i)==1:
        point.append(i)
        break
for i in y:
    if y.count(i)==1:
        point.append(i)
        break
print(point[0],point[1])
