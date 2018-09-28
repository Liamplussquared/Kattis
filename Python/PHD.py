#https://open.kattis.com/problems/helpaphd
for i in range(int(input())):
    p = input()
    if p == "P=NP": print("skipped")
    else:
        problem = p.split("+")
        print(int(problem[1])+int(problem[0]))
