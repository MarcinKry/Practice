def mergeOverlappingIntervals(intervals):
    # O(nlogn) time | O(n) space
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    #Sort the intervals by starting value
    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals: 
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval
        
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else: 
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)
            
    return mergedIntervals

intervals=[ [ 1, 2], [3, 5], [4, 7], [6, 8], [9, 10] ]
print(mergeOverlappingIntervals(intervals))