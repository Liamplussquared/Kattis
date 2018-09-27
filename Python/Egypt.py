#https://open.kattis.com/problems/egypt
while 1:
  sides = [int(x) for x in input().split()]
  h = max(sides)
  sides.remove(h)
  if h == 0: break

  if(h**2 == (sides[0]**2 + sides[1]**2)): print("right")
  else: print("wrong")