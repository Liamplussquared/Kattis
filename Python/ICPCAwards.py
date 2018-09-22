#https://open.kattis.com/problems/icpcawards
unis = int(input())
uniNames = []
count = int(0)
while unis:
    team = input().split()
    if not team[0] in uniNames and count<12:
        uniNames.append(team[0])
        print(team[0]+" "+team[1])
        count+=1
    unis -=1
