for i in range(0, int(input())):
	numGuests = int(input())
	paired = set()
	invNums = input().split()
	for num in invNums:
		if num in paired:
			paired.remove(num)
		else:
			paired.add(num)
	for _ in paired: odd = _
	print ('Case #%d: %d' % (i+1, int(odd)))