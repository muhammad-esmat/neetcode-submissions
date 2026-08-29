class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}

        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1 
            
        sortedFreq = sorted(freqDict.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in sortedFreq[:k]]

