from binarytree import build
class Solution(object):
    def maxDepth(self, root):
        if root==None: return 0
        queue=[[root,1]]
        Max=1
        while(queue):
            curr,depth=queue.pop(0)
            if curr.left!=None:
                queue.append([curr.left,depth+1])
                Max=max(Max,depth+1)
            if curr.right!=None:
                queue.append([curr.right,depth+1])
                Max=max(Max,depth+1)
        return Max        
if __name__ == "__main__":
    obj=Solution()
    arr1=[1,3,2,5]
    arr2=[2,1,3,None,4,None,7]
    root1=build(arr1)
    root2=build(arr2)
    M_root=obj.maxDepth(root1)
    print(M_root)
    print(build([90,69,None,49,89,None,52,None]))