from collections import defaultdict
class Solution(object):
    def countSubTrees(self, n, edges, labels):
        graph=defaultdict(list)
        visited=[False]*n
        Op=[0]*n        
        for x in edges:
            graph[x[1]]+=[x[0]]
            graph[x[0]]+=[x[1]]
        def traverse(src):
            visited[src]=True
            Lab=[[0 for i in range(26)]]
            Lab_i=[]
            for x in graph[src]:
                if( visited[x]==False):
                    Lab_i=traverse(x)
                    Lab+=Lab_i
            T_lab=[sum(x) for x in zip(*Lab)]
            T_lab[ord(labels[src])-97]+=1          
            Op[src]=T_lab[ord(labels[src])-97]
            return [T_lab]
        LAB=traverse(0)
        return Op

if __name__ == "__main__":
    obj=Solution()
    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    labels = "abaedcd"    
    #root=build(arr)
    #print(root)
    Op=obj.countSubTrees(n,edges,labels)
    print(Op)