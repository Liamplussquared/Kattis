input = input().split()
rounds = int(input[0])
score = int(input[1]) + int(input[2])
if score//rounds % 2 == 0: 
	print("paul")
else:
	print("opponent")