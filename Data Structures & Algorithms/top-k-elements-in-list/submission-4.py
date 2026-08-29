class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resultDict = {}

        for num in nums:
            resultDict[num] = resultDict.get(num, 0) + 1

        sortedDict = sorted(resultDict.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in sortedDict[:k]]

