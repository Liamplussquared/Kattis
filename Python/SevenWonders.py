#https://open.kattis.com/problems/sevenwonders
cards = input()
score = cards.count("T")**2 + cards.count("C")**2 + cards.count("G")**2 
differentSets = min(cards.count("T"),cards.count("C"),cards.count("G"))
score += differentSets*7
print(score)