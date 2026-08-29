class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
    
        resultDict = defaultdict(int)
    
        for num in nums:
            resultDict[num] += 1
    
        sortedDict = sorted(resultDict.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in sortedDict[:k]]
    
