#https://open.kattis.com/problems/mirror
count = int(0)
for i in range(int(input())):
  count+=1
  l = []
  size = [int (x) for x in input().split()]
  for j in range(size[0]):
    l.append(input())
  l.reverse()
  result = ""
  print("Test " + str(count))
  for k in l:
    print(k[::-1]) #returns reverse value of string