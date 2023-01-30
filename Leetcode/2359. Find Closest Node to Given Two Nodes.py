class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        reach1=[]
        visited=[True]*len(edges)
        dist_node1,i=dict(),0
        while( visited[node1]):
            reach1.append(node1)
            dist_node1[node1]=i
            if edges[node1]==-1: break
            visited[node1]=False
            node1=edges[node1]
            i+=1
        reach2=[]
        visited=[True]*len(edges)
        dist_node2,i=dict(),0
        while(visited[node2]):
            reach2.append(node2)
            dist_node2[node2]=i
            if edges[node2]==-1:  break
            visited[node2]=False
            node2=edges[node2]
            i+=1        
        Min,ndx=len(edges)+1,len(edges)+1
        for i in reach1:
            if i not in dist_node2: continue
            Max=max(dist_node1[i],dist_node2[i])
            if( Max< Min ):
                Min=Max
                ndx=i
            elif Max==Min:
                if i<ndx: ndx=i
        if ndx==len(edges)+1: return -1
        return ndx
if __name__ == "__main__":
    obj=Solution()
    edges = [2,2,3,-1]
    node1=0
    node2=1
    Op=obj.closestMeetingNode(edges,node1,node2)
    print(Op)