import time
class Solution(object):
    def unique(self, s):
        id=[0]*127
        for x in s:
            id[ord(x)]+=1
            if(id[ord(x)]>1):
                return False
            
        return True            
    def lengthOfLongestSubstring(self, s):
        s=list(s)
        max_s,cs=0,0
        for start in range(len(s)):
            for end in range(start,len(s)):
                if(max_s==95):
                    return max_s
                if (self.unique(s[start:end+1])):
                    cs=(end-start)+1
                    max_s=max(cs,max_s)
                else:
                    break
        return max_s

        
if __name__ == "__main__":
    st=time.time()
    obj=Solution()    
    Op=obj.lengthOfLongestSubstring("s")
    print(Op)
    print("--- %s seconds ---" % (time.time() - st))