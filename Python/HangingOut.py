#https://open.kattis.com/problems/hangingout
info = input().split()
L = int(info[0])
people = 0
denied = 0
for i in range(int(info[1])):
    group = input().split()
    if group[0] == "enter":
        if people + int(group[1]) > L:
            denied+=1
        else: people += int(group[1])
    else:
        people-=int(group[1])
print(denied)
