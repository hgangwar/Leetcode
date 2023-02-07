class Solution(object):
    def vowelStrings(self, words, queries):
        n=len(words)
        Pre=[0]*(n+1)
        for i,x in enumerate(words):
            if x[0].lower() in ('a', 'e', 'i', 'o', 'u') and x[-1].lower() in ('a', 'e', 'i', 'o', 'u'):
                Pre[i]=Pre[i-1]+1
            else: Pre[i]=Pre[i-1]
        Ans=[0]*len(queries)
        for i,x in enumerate(queries):
            Ans[i]=Pre[x[1]]-Pre[x[0]-1]
        return Ans
if __name__ == "__main__":
    obj=Solution()
    Op=obj.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]])
    print(Op)