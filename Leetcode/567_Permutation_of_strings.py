from itertools import permutations
class Solution(object):
    def getID(self, s1):
        id=[0]*26
        for x in s1:
            id[ord(x)-97]+=1
        return id
    def checkInclusion(self, s1, s2):
        s1, s2=list(s1), list(s2)
        s1_ID=self.getID(s1)
        for start in range(0,len(s2)):
            if( start+len(s1)<=len(s2)):
                s2_ID=self.getID(s2[start:start+len(s1)])
                if s1_ID==s2_ID:
                    return True
        return False
                
            
if __name__ == "__main__":
    obj=Solution()
    s1 = "dinitrophenylhydrazine"
    s2 = "acetylphenylhydrazine"
    Op=obj.checkInclusion(s1,s2)
    print(Op)
