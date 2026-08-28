class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        resultDic = defaultdict(list)
        
        for i in range(n):
            count = [0] * 26
    
            for c in strs[i]:
                count[ord(c) - 97] += 1
    
            resultDic[tuple(count)].append(strs[i])
            
        return list(resultDic.values())
        
