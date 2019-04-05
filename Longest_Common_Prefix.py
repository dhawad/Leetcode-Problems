"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==0):
            return ""
        s1=strs[0]
        for i in range(1,len(strs)):
            s=""
            s2=strs[i]
            
            for j in range(0,min(len(s2),len(s1))):
                if(s1[j]!=s2[j]):
                    break
                else:
                    s=s+s1[j]
            s1=s
                    
            

        return s1
                
        
