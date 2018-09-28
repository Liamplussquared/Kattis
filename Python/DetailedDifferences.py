#https://open.kattis.com/problems/detaileddifferences
for i in range(int(input())):
    a = input()
    b = input()
    count = 0
    result = ""
    for _ in a:
        if _!=b[count]: result+="*"
        else: result+="."
        count+=1
    print (a)
    print(b)
    print(result)
    print("")