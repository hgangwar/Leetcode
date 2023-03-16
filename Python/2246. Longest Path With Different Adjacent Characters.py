class Solution(object):
    def longestPath(self, parent, s):       
        n, self.ans=len(parent),1
        Tree=[[] for i in range(n)]
        for i in range(1,n):
            x=parent[i]
            Tree[x]+=[i]
        def traverse(src):
            m1,m2=0,0
            for x in Tree[src]:
                res=traverse(x)
                if (s[x]==s[src]):
                    continue
                if(res>m1):
                    m2=m1
                    m1=res
                elif(res>m2):
                    m2=res
            self.ans=max(self.ans,1+m1+m2)
            return m1+1     
        traverse(0)
        return self.ans

if __name__ == "__main__":
    obj=Solution()
    parent=[1,0,0,1,1,2]
    s="abacbe"
    Op=obj.longestPath(parent,s)
    print(Op)