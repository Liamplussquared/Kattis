cases = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(cases):
    missing = ""
    sentence = input().lower()
    for letter in alphabet:
        if letter not in sentence:
            missing += letter
    if missing == "":
        print ("pangram")
    else:
        print("missing " + missing)
        


