#https://open.kattis.com/problems/eligibility
for i in range(int(input())):
  c = input().split()
  #0 = name, 1 = secondary, 2 =DOB, 3=modules

  if int(c[1][0:4]) >= 2010: 
    print(c[0] + " eligible")
  elif int(c[2][0:4]) >= 1991:
    print(c[0] + " eligible")
  elif int(c[3]) >= 41:
    print(c[0] + " ineligible")
  else:
    print(c[0] + " coach petitions")