from collections import defaultdict
class Solution(object):
    def exist(self, board, word):
        Graph=defaultdict(list)
        m,n=len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                Graph[board[i][j]]+=[(i*n)+j]
        def near(i,j,ndx):
            ls=[]
            if(j>0):
                if board[i][j-1]==word[ndx]: ls+=[[i,j-1]] 
            if(j<n-1):
                if board[i][j+1]==word[ndx]: ls+=[[i,j+1]]
            if(i>0):
                if board[i-1][j]==word[ndx]: ls+=[[i-1,j]]
            if(i<m-1):
                if board[i+1][j]==word[ndx]: ls+=[[i+1,j]]
            return ls
        def dfs(i,j,ndx,Tar,path):
            if ndx==Tar: return True
            Near=near(i,j,ndx)
            for x in Near:
                key=(x[0]*n)+x[1]
                if not key in path:
                    ans=dfs(x[0],x[1],ndx+1,Tar,path+[key])
                    if ans: return True
            return False
        if word[0] not in Graph: return False
        for x in word:
            if x not in Graph: return False
        else:
            for y in Graph[word[0]]:
                Ans=dfs(y//n,y%n,1,len(word),[y])
                if Ans: return True
        return False
if __name__ == "__main__":
    obj=Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
    word = "ABCB"
    Op=obj.exist(board,word)
    print(Op)



        