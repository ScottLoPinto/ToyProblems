# Have the function SwitchSort(arr) take arr which will be an an array consisting of integers 
# 1...size(arr) and determine what the fewest number of steps is in order to sort the array 
# from least to greatest using the following technique: Each element E in the array can swap 
# places with another element that is arr[E] spaces to the left or right of the chosen element.
# You can loop from one end of the array to the other. For example: if arr is the array [1, 3, 4, 2] 
# then you can choose the second element which is the number 3, and if you count 3 places to the left you'll 
# loop around the array and end up at the number 4. Then you swap these elements and arr is then [1, 4, 3, 2]. 
# From here only one more step is required, you choose the last element which is the number 2, count 2 places 
# to the left and you'll reach the number 4, then you swap these elements and you end up with a sorted array 
# [1, 2, 3, 4]. Your program should return an integer that specifies the least amount of steps needed in order 
# to sort the array using the following switch sort technique.
# The array arr will at most contain five elements and will contain at least two elements.

def switch_sort(arr):
	# if ( index_current +- num ) % arr.len == desired_index, then swap and ++ swaps
	# if new_arr == sorted_arr, return swaps
	swaps = 0
	sorted_arr = sorted(arr)

	while(arr != sorted_arr):
		for i in range(len(arr)):
			
			idx_right = (i + arr[i]) % len(arr)
			idx_left = (i - arr[i]) % len(arr)
			idx_desired = arr[i]-1

			if(arr[i] == sorted_arr[i]):
				continue

			elif(idx_right == idx_desired):
				temp = arr[i]
				arr[i] = arr[idx_right]
				arr[idx_right] = temp
				swaps+=1

			elif(idx_left == idx_desired):
				temp = arr[i]
				arr[i] = arr[idx_left]
				arr[idx_left] = temp
				swaps+=1
	return swaps
