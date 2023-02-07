class Solution(object):
    def letterCasePermutation(self, s):
        output=[""]
        for c in s:
            t=[]
            if c.isalpha():
                for o in output:
                    t.append(o+c.upper())
                    t.append(o+c.lower())
            else:
                for o in output:
                    t.append(o+c)
            output=t
        return output
if __name__ == "__main__":
    obj=Solution()
    s = "a1b2"
    Op=obj.letterCasePermutation(s)
    print(Op)
