class Solution:
    def rangeAddQueries(self, n, queries):
        ans = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                ans[r][c1] += 1
                if c2 + 1 < n: 
                    ans[r][c2 + 1] -= 1
        for r in range(n):
            for c in range(1, n):
                ans[r][c] += ans[r][c - 1]
        return ans
if __name__ == "__main__":
    obj=Solution()
    n = 3
    queries = [[1,1,2,2],[0,0,1,1]]
    Op=obj.rangeAddQueries(n,queries)
    print(Op)