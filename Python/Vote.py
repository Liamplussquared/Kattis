#https://open.kattis.com/problems/vote
for i in range(int(input())):
    candidates = int(input())
    votes = [int(input()) for _ in range (candidates)]
    if votes.count(max(votes)) > 1:
        print("no winner")
    else:
        winner = max(votes)
        if((winner / sum(votes)) > 0.5):
            print("majority winner " + str(votes.index(winner)+1))
        else: 
            print("minority winner " + str(votes.index(winner)+1))