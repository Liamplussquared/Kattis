#https://open.kattis.com/problems/grassseed
costMeter = input()
numberLawns = int(input())
area = float(0)
while numberLawns:
    lawn = input().split()
    area += float(lawn[0]) * float(lawn[1])
    numberLawns -= 1
print(area * float(costMeter))