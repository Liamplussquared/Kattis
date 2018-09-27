#https://open.kattis.com/problems/sumoftheothers
while True:
  try:
    n = [int(i) for i in input().split()]
  except EOFError:
    exit() 
  s = sum(n) 
  for v in n:
    if s - v == v: #if sum of all others
      print(v)
      break