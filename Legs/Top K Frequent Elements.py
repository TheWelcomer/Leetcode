def topKFrequent(nums, k):
    result = []
    freqList = [[] * len(nums)]
    freqCounter = 0
    for i in range(len(nums) - 1):
        if nums[i + 1] == nums[i]:
            freqCounter += 1
        else:
            freqList[freqCounter].append(nums[i])
            freqCounter = 0

    for numList in reversed(freqList):
        for num in numList:
            if len(result) == k:
                return result
            result.append(num)
    return result
print(topKFrequent([1,1,1,2,2,3],2))