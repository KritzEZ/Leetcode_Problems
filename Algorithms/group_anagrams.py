class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        if strs is None: return 
        ans = [[strs[0]]]
        
        firstword = sorted(strs[0])
        firstwordsort = "".join(firstword)
        
        letterholder = [firstwordsort]
        
        for i in range(1, len(strs)):
            wordarr = sorted(strs[i])
            sortword = "".join(wordarr)
            
            if sortword in letterholder:
                ans[letterholder.index(sortword)].append(strs[i])
            else:
                letterholder.append(sortword)
                ans.append([strs[i]])
                
        return ans