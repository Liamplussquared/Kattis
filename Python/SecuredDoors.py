#https://open.kattis.com/problems/securedoors
events = int(input())
changes = {}
for _ in range(events):
  event = input().split()
  change = event[0]
  name = event[1]

  if change == "entry": #entering
    if name not in changes:
      changes[name] = True
      print(name + " entered")
    elif changes[name]==True:
      print(name + " entered (ANOMALY)")
    else:
      changes[name] = True
      print(name + " entered")
  else: #leaving
    if name not in changes:
      changes[name] = False
      print(name + " exited (ANOMALY)")
    elif changes[name]==False:
      print(name + " exited (ANOMALY)")
    else:
      print(name + " exited")
      changes[name] = False