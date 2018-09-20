import math

testCase = input().split(" ")
h = int(testCase[0])
v = int(testCase[1])

print(math.ceil(h / math.sin(math.radians(v))))