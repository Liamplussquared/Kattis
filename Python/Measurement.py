#https://open.kattis.com/problems/measurement
nums = input().split()
standard = {
    "thou":1, "th":1,
    "inch":1000, "in":1000,
    "foot":12000, "ft":12000,
    "yard":36000, "yd": 36000,
    "chain":792000, "ch":792000,
    "furlong":7920000, "fur": 7920000,
    "mile":63360000, "mi": 63360000,
    "league": 190080000, "lea": 190080000
}
revert = {
    "thou":1, "th":1,
    "inch":1/1000, "in":1/1000,
    "foot":1/12000, "ft":1/12000,
    "yard":1/36000, "yd": 1/36000,
    "chain":1/792000, "ch":1/792000,
    "furlong":1/7920000, "fur": 1/7920000,
    "mile":1/63360000, "mi": 1/63360000,
    "league": 1/190080000, "lea": 1/190080000
}

inth = int(nums[0]) * standard[nums[1]]
back = float(inth) * revert[nums[3]]
print(back)