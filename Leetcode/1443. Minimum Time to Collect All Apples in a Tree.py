import collections
class Solution(object):
    def minTime(self, n, edges, hasApple):
        appLen=[0]*n
        visited=[False]*n
        tree=collections.defaultdict(list)
        for x in edges:
            tree[x[0]]+=[x[1]]
            tree[x[1]]+=[x[0]]
        def traverse(src):
            visited[src]=True
            flag=0
            for x in tree[src]:
                if visited[x]==False:
                    flag=1
                    break
            if(flag==0 and hasApple[src]==False):
                return 0
            elif not (src in tree):
                appLen[src]=2
                return 2
            else:
                if(hasApple[src]):
                    appLen[src]=2
                x=tree[src]
                Sum=0
                for i in x:
                    if not visited[i]:
                        Sum+=traverse(i)
                appLen[src]=max(appLen[src],Sum)
                if(appLen[src]!=0 and Sum!=0): 
                    return appLen[src]+2
                else:
                    return appLen[src]
        return max(traverse(0)-2,0)
if __name__ == "__main__":
    obj=Solution()
    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False,False,True,False,True,True,False]
    Op=obj.minTime(n, edges, hasApple)
    print(Op)