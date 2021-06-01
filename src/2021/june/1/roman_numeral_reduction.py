# Have the function RomanNumeralReduction(str) read str which will be a string of roman numerals in decreasing order. 
# The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000.
# Your program should return the same number given by str using a smaller set of roman numerals. 
# For example: if str is "LLLXXXVVVV" this is 200, so your program should return CC because this is the shortest way to write 200 using the roman numeral system given above. 
# If a string is given in its shortest form, just return that same string.

def roman_numeral_reduction(str):
	#a possible method for solving this is to iterate through the string once and get the value of the string, then divide it up
	#in decreasing order
	numdict = {
		"I" : 1,
		"V" : 5,
		"X" : 10,
		"L" : 50,
		"C" : 100,
		"D" : 500,
		"M" : 1000,
	}
	value = 0
	correctStr = ""
	for char in str:
		value += numdict[char]
	
	while(value!=0):
		
		M = value//1000
		value = value - M*1000
		
		D = value//500
		value = value - D*500
		
		C = value//100
		value = value - C*100
		
		L = value//50
		value = value - L*50
		
		X = value//10
		value = value - X*10
		
		V = value//5
		value = value - V*5
		
		I = value//1
		value = value - I*1

		correctStr = 'M'*M + 'D'*D + 'C'*C + 'L'*L + 'X'*X + 'V'*V + 'I'*I

	# this method will work very well, i dont know what the time complexity of replace is but i imagine it is not good
	# googled it and the time complexity of str.replace in this case is close to O(n*(1 + e)) where e is between .5 and .2
	#str = str.replace("IIIII", "V")
	#str = str.replace("VV", "X")
	#str = str.replace("XXXXX", "L")
	#str = str.replace("LL", "C")
	#str = str.replace("CCCCC", "D")
	#str = str.replace("DD", "M")

	return correctStr
