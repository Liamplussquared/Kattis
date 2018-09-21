#https://open.kattis.com/problems/kemija08
code = input()
vowels = "aeiou"
ignore = int(0)
decoded = ""
for letter in code:
    if ignore:
        ignore-=1
    elif letter in vowels: #ignore next two letters
        decoded += letter
        ignore = 2
    else: 
        decoded += letter
print(decoded)

