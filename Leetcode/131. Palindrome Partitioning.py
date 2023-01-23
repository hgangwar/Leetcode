class Solution:
    def partition(self, s):
        ans= []
        def isPalindrome(s):
            return s == s[::-1]
        def dfs(s , j, path, ans):
            if j == len(s):
                ans.append(path)
                return
            for i in range(j, len(s)):
                if isPalindrome(s[j: i + 1]):
                    dfs(s, i + 1, path + [s[j: i + 1]], ans)
        dfs(s, 0, [], ans)
        return ans
if __name__ == "__main__":
    obj=Solution()
    Op=obj.partition("aab")
    print(Op)
