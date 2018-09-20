#https://open.kattis.com/problems/alphabetspam
spam = input()
lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count_w = 0
count_l = 0
count_u = 0
count_s = 0

for character in spam:
    if character in lowerCase:
        count_l +=1
    elif character in upperCase:
        count_u +=1
    elif character=="_":
        count_w +=1
    else:
        count_s +=1

print(count_w / len(spam))
print(count_l / len(spam)) 
print(count_u/ len(spam))
print(count_s / len(spam))
