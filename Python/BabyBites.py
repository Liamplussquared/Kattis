#babybites
throwaway = input()
speech = input().split()
count = 0
check = True
for word in speech: 
  count += 1
  if word != "mumble":
    if int(word) != int(count):
      print("something is fishy")
      check = False
      break
if check: print("makes sense")