class Solution(object):
    def wordPattern(self, pattern, s):
        ls=list(s.split())
        Dict=dict()
        Dict2=dict()
        if(len(ls)!=len(pattern)):
            return False
        for i in range(len(ls)):
            key=pattern[i]
            if not (key in Dict):
                if not ls[i] in Dict2:
                    Dict[key]=ls[i]
                    Dict2[ls[i]]=key
                else:
                    return False
            else:
                if Dict[key]!=ls[i]:
                    return False
        return True
if __name__ == "__main__":
    obj=Solution()
    pattern = "abba"
    s = "dog dog dog dog"
    Op=obj.wordPattern(pattern,s)
    print(Op)
