class Solution(object):
    def getID(self, s1):
        id=[0]*26
        for x in s1:
            id[ord(x)-97]+=1
        return id
    def findAnagrams(self, s, p):
        if len(p)>len(s): return []
        pID=self.getID(p)
        Wid=self.getID(s[0:len(p)])
        matches=0
        for i in range(0,26):
            if pID[i]==Wid[i]: matches+=1
        Ans=[]
        if matches==26: Ans.append(0)
        ndx=len(p)
        while(ndx<len(s)):
            Wid[ord(s[ndx])-97]+=1
            if Wid[ord(s[ndx])-97]==pID[ord(s[ndx])-97]:    matches+=1
            elif Wid[ord(s[ndx])-97]==pID[ord(s[ndx])-97]+1: matches-=1
            Wid[ord(s[ndx-len(p)])-97]-=1
            if Wid[ord(s[ndx-len(p)])-97]==pID[ord(s[ndx-len(p)])-97]:  matches+=1
            elif Wid[ord(s[ndx-len(p)])-97]==pID[ord(s[ndx-len(p)])-97]-1: matches-=1
            if matches==26:  Ans.append(ndx-len(p)+1)
            ndx+=1
        return Ans
if __name__ == "__main__":
    obj=Solution()
    Op=obj.findAnagrams(s = "bpaa", p = "aa")
    print(Op)