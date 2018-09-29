#https://open.kattis.com/problems/patuljci
nums = []
for i in range(9):
    nums.append(int(input()))
for i in range(9):
    for j in range(i+1,9):
        if sum(nums) -(nums[i] +nums[j])==100:
            a = nums[i]
            b = nums[j]
for i in nums:
    if not(i == a or i == b):
        print(i)