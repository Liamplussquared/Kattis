#https://open.kattis.com/problems/nodup
sentence = input().split(" ")
words = set()
check = True
for word in sentence:
    if word in words:
        print("no")
        check = False
        break
    else:
        words.add(word)
if check:
    print("yes")