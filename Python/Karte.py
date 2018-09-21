#https://open.kattis.com/problems/karte
import textwrap
cards = textwrap.wrap(input(), 3)
p = k = h = t = int(13)
check = True
for card in cards:
    if cards.count(card) > 1:
        print("GRESKA")
        check = False
        break
    else:
        if "P" in card: p-=1
        elif "K" in card: k-=1
        elif "H" in card: h-=1
        else: t-=1
if check: print(p,k,h,t)
#p k h t 