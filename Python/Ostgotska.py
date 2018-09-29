#https://open.kattis.com/problems/ostgotska
s = input().split() #words
c = int(0)
for _ in s: 
    if "ae" in _: 
        c+=1
print("dae ae ju traeligt va") if c/len(s) >= 0.4 else print("haer talar vi rikssvenska")