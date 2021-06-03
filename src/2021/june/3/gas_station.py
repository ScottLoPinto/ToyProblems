# Have the function GasStation(strArr) take strArr which will be an an array consisting of the following elements: 
# N which will be the number of gas stations in a circular route and each subsequent element will be the string g:
# c where g is the amount of gas in gallons at that gas station and c will be the amount of gallons of gas needed to get to the following gas station.
# For example strArr may be: ["4","3:1","2:2","1:2","0:1"]. Your goal is to return the index of the starting gas station that will allow you to travel around the whole route once, 
# otherwise return the string impossible. For the example above, there are 4 gas stations, and your program should return the string 1 because starting at station 1 you receive 
# 3 gallons of gas and spend 1 getting to the next station. Then you have 2 gallons + 2 more at the next station and you spend 2 so you have 2 gallons when you get to the 3rd station. 
# You then have 3 but you spend 2 getting to the final station, and at the final station you receive 0 gallons and you spend your final gallon getting to your starting point. 
# Starting at any other gas station would make getting around the route impossible, so the answer is 1. If there are multiple gas stations that are possible to start at, 
# return the smallest index (of the gas station). N will be >= 2.

def gas_station(strArr):
	# number of stations
	stations = int(strArr[0])
	#array without the number of stations
	adjusted = strArr[1::]
	#split so that larger numbers dont ruin everything
	adjusted = [k.split(':') for k in adjusted]
	nodes = 0
	edges = 0
	#for loop to check if its impossible
	for i in range(1,stations):
			edges += int(adjusted[i][1])
			nodes += int(adjusted[i][0])			
	if(nodes < edges):
		return "impossible"

	#for loop to check the route by checking if each starting point is valid
	#starting from the smallest index so that if it gets to the end it returns
	#note: the problem/tests dont seem to account for the opposite direction of travel
	#which is fine because i think that would make this considerably more challenging
	for i in range(stations):
		temp_edge = 0
		temp_node = 0
		for j in range(stations):
			temp_edge += int(adjusted[((i + j)%stations)][1])
			temp_node += int(adjusted[((i + j)%stations)][0])
			if( temp_edge > temp_node):
				break
		if(temp_edge<= temp_node):
			return i+1

