class Solution(object):
    def bfs(self, Ad,mat,D,a,b):
        r,c=len(mat),len(mat[0])
        x=(a*c)+b
        queue, visited=[],[False]*(r*c)
        queue.append(x)
        visited[x]=True
        while(queue):
            s=queue.pop(0)
            for x in Ad[s]:
                if(visited[x]==False):                    
                    m,n=x//c,x%c
                    if (abs(m-a)+abs(n-b))==(r+c-2):
                        return r+c-2
                    if(D[m][n]==0):
                        return abs(m-a)+abs(n-b)
                    queue.append(x)
                    visited[x]=True
    def updateMatrix(self, mat):
        r,c=len(mat),len(mat[0])
        n,k=r*c,0
        Ad=[[] for i in range(n)]
        D=[[-1 for i in range(c)] for j in range(r)]
        for i in range(0,r):
            for j in range(0,c):
                if mat[i][j]==0:
                    k+=1
                    g,h=i,j
                    D[i][j]=0
                x=(i*c)+j                 
                if(j>0):
                    Ad[x]+=[x-1]                    
                if(j<c-1):
                    Ad[x]+=[x+1]                    
                t=((i-1)*c)+j
                d=((i+1)*c)+j
                
                if(i>0):
                    Ad[x]+=[t]                    
                if(i<r-1):
                    Ad[x]+=[d]
        
        
        for i in range(0,r):
            for j in range(0,c):
                if(D[i][j]==0):
                    continue
                if(k==1):
                    D[i][j]=abs(g-i)+abs(h-j)
                else:
                    D[i][j]=self.bfs(Ad,mat,D,i,j)
        return D

if __name__ == "__main__":
    obj=Solution()
    mat=[]
    Op=obj.updateMatrix(mat)
    print(Op)




""" c++ DP solution
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        if (rows == 0) 
            return matrix;
        int cols = matrix[0].size();
        vector<vector<int>> dist(rows, vector<int> (cols, INT_MAX - 100000));

        //First pass: check for left and top
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    dist[i][j] = 0;
                } else {
                    if (i > 0)
                        dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1);
                    if (j > 0)
                        dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1);
                }
            }
        }

        //Second pass: check for bottom and right
        for (int i = rows - 1; i >= 0; i--) {
            for (int j = cols - 1; j >= 0; j--) {
                if (i < rows - 1)
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1);
                if (j < cols - 1)
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1);
            }
        }
        return dist;
    }
};
"""