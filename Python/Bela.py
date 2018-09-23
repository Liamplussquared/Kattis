#https://open.kattis.com/problems/bela
dominant = {"A":"11","K":"4","Q":"3","J":"20","T":"10","9":"14","8":"0","7":"0"}
nonDominant = {"A":"11","K":"4","Q":"3","J":"2","T":"10","9":"0","8":"0","7":"0"}
n = input().split()
numHands = int(n[0])
dom = n[1]
score = int(0)
for i in range (4*numHands):
    hand = input()
    if hand[1] == dom:
        score += int(dominant[hand[0]])
    else:
        score += int(nonDominant[hand[0]])
print(score)
