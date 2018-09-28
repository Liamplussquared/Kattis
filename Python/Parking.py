#https://open.kattis.com/problems/parking2
for _ in range(int(input())):
    slots = input() #don't need it 
    nums = [int(x) for x in input().split()]
    print(2*(max(nums)-min(nums)))