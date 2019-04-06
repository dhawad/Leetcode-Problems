'''Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if(len(needle)==0):
            return 0
        elif(len(haystack)<len(needle)):
            return -1
        
        ned_l=0
        j=0
        k=0
        for i in range(0,len(haystack)):
            k=i
            while(ned_l<len(needle) and k<len(haystack) and j<len(needle)):
                if(haystack[k]==needle[j]):
                    k+=1
                    j+=1
                    ned_l+=1
                else:
                    j=0 
                    break
            if(ned_l==len(needle)):
                return i
            else:
                ned_l=0
                continue
                
        return -1

               
                
                    
                
        
                
                
                
                
                        
                
        
        
 
        
                
                
        
        
