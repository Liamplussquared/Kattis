#returns sum of digits
def sum(i):
    s = str(i)
    r = 0
    for c in s:
        r += int(c)
    return r

n = 1
while n != 0:
    n = int(input())
    if(n == 0): break #avoid printing 11
    target = sum(n) #sum of digits of n
    p = 11
    found = True

    while found:
        if sum(n * p) == target:
            print(p)
            found = False
        else:
            p+=1

