#https://open.kattis.com/problems/apaxiaaans
name = input()
brief = name[0]
for letter in name:
    if brief[len(brief)-1] != letter:
        brief+=letter
print(brief)
