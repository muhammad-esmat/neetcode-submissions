class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        resultDic = {}
    
        for i in range(n):
            strSet = "".join(sorted(strs[i]))
            
            try:
                resultDic[strSet].append(strs[i])
            except:
                resultDic[strSet] = [strs[i]]
    
        return list(resultDic.values())
    
