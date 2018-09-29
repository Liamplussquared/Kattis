#https://open.kattis.com/problems/datum
import calendar
date = input().split()
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(days[calendar.weekday(2009, int(date[1]), int(date[0]))])