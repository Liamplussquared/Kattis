#https://open.kattis.com/problems/dicecup
faces = input().split()
N = int(faces[0])
M = int(faces[1])
results = []
for i in range(N):
    for j in range(M):
        results.append(int(i+j+2))
#now need to find occurences 
results = sorted(results) ##all results
numbers = set(results) #all unique results
maxOccurence = int(0)

for i in numbers: #find maxOccurence
    if results.count(i) > maxOccurence:
        maxOccurence = results.count(i)
for i in numbers:
    if results.count(i) == maxOccurence: #deal with multiple modes
        print (i)

