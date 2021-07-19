"""
Max Subset Sum No Adjacent
Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array.
If the input array is empty, the function should return 0.
Sample Input: 
array = [75, 105, 120, 75, 90, 135]
Sample Output:
330 // 75 + 120 + 135
"""

def maxSubsetSumNoAdjacent(array):
	#O(n) time | o(n) space
	if not len(array):
		return 0
	elif len(array)==1:
		return array[0]
	maxSums = array[:]
	maxSums[1] = max(array[0], array[1])
	for i in range(2,len(array)):
		maxSums[i] = max(maxSums[i-1], maxSums[i-2]+ array[i])
	return maxSums[-1]
