#https://open.kattis.com/problems/modulo
uniqueNumbers = []
count = 0
for i in range(10):
    n = input()
    modulo = int(n)%42
    if modulo not in uniqueNumbers:
        count +=1
        uniqueNumbers.append(modulo)
print(count)

        

