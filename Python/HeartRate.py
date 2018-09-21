#https://open.kattis.com/problems/heartrate
testCases = int(input())
while testCases:
    case = input().split()
    beats = float(case[0])
    seconds = float(case[1])
    shortestTime = seconds / (beats - 1.0) #started at end of beat
    largestTime = seconds / (beats + 1.0) #started on a beat
    print(60.0/shortestTime, (60*beats) / seconds, 60.0/largestTime)
    testCases -=1