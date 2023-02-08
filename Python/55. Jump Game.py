from collections import defaultdict
class Solution(object):
    def canJump(self, nums):
        graph=defaultdict(int)
        n=len(nums)
        for i,x in enumerate(nums):
            if x==0: continue
            graph[x]+=i+x
        queue=[[0]]
        while queue:
            path=queue.pop()
            key=path[-1]
            if key==n-1:
                return True
            for x in graph[key]:
                if not x in path:
                    queue.append(path+x)
        return False
if __name__ == "__main__":
    obj=Solution()
    Op=obj.canJump(nums = [3,2,1,0,4])
    print(Op)