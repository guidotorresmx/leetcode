class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        setGroups = set()
        
        for s in strs:
            setGroups.add("".join(sorted(s)))
        
        dictGroups = dict()
        for sG in setGroups:
            dictGroups[sG] = []
        
        for s in strs:
            key = "".join(sorted(s))
            dictGroups[key].append(s)
        
        return list(dictGroups.values())
            
