# Have the function KaprekarsConstant(num) take the num parameter being passed which will be a 4-digit number with at 
# least two distinct digits. Your program should perform the following routine on the number: Arrange the digits in 
# descending order and in ascending order (adding zeroes to fit it to a 4-digit number), and subtract the smaller number 
# from the bigger number. Then repeat the previous step. Performing this routine will always cause you to reach a 
# fixed number: 6174. Then performing the routine on 6174 will always give you 6174 (7641 - 1467 = 6174). 
# Your program should return the number of times this routine must be performed until 6174 is reached. 
# For example: if num is 3524 your program should return 3 because of the following steps: 
# (1) 5432 - 2345 = 3087, (2) 8730 - 0378 = 8352, (3) 8532 - 2358 = 6174.

def kaprekars_constant(num):
	count = 0
	while(num != 6174):
		#if num < 4 digits, add a 0 to the end
		while(num - 999 <= 0):
			num = num*10
		
		#list of integers
		numList = [int(digit) for digit in str(num)]  
		
		#get ascending order number
		numList.sort()
		strList = [str(digit) for digit in numList]
		asc = int("".join(strList))

		#get descending order number
		numList.sort(reverse=True)
		strList = [str(digit) for digit in numList]
		des = int("".join(strList))

		#update num
		num = des - asc
		count+=1
	return count
