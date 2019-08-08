numTestCases = int(input())
while numTestCases > 0:
	check = input()[::-1] #reverse input
	output = ''
	#start at start of string, double every second digit
	for i in range(0, len(check)):
		if i % 2 != 0:
			intVal = 2 * int(check[i])
			if intVal > 9:
				#change value at position to sum of digits in intVal
				newVal = int(str(intVal)[0]) + int(str(intVal)[1])
				output += str(newVal)
			else:
				output += str(intVal)
		else:
			output += check[i]
	
	sumDigits = 0
	for _ in output:
		sumDigits += int(_)
	
	if sumDigits % 10 ==0:
		print("PASS")
	else:
		print("FAIL")
	
		
	numTestCases -= 1

	
