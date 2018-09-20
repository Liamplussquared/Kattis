#https://open.kattis.com/problems/everywhere

n = int(input()) #number test cases

while n:
    numCities = int(input())
    cities = []
    count = 0
    for i in range(numCities):
        city = input()
        if city not in cities:
            cities.append(city)
            count += 1
    print(count)
    n -= 1