from collections import deque
class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)
        def next_square(step):
            quot, rem = divmod(step-1, n)
            row = (n-1)-quot
            if row%2!=n%2:
                col = rem 
            else:
                col = (n - 1) - rem
            return row, col
        dist = {1: 0}
        queue = deque([1])
        while queue:
            square = queue.popleft()
            if square == n*n:
                return dist[square]
            for new_square in range(square+1, min(square+6, n*n) + 1):
                r, c = next_square(new_square)
                if board[r][c] != -1:
                    new_square = board[r][c]
                if new_square not in dist:
                    dist[new_square] = dist[square] + 1
                    queue.append(new_square)
        return -1      
if __name__ == "__main__":
    obj=Solution()
    board = [[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]
    Op=obj.snakesAndLadders(board)
    print(Op)