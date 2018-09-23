#https://open.kattis.com/problems/conundrum
text = input()
count = int(0)
per = "PER"
for i in range (len(text)):
    letter = text[i]
    n = i % 3
    if letter != per[i%3]:
        count+=1
print(count)