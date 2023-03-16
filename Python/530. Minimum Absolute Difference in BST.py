from binarytree import build
class Solution(object):
    def getMinimumDifference(self, root):
        Min=1e09
        arr=[root.val]
        queue=[root]
        while(queue):
            curr=queue.pop(0)
            if curr.left!=None:
                queue.append(curr.left)
                arr.append(curr.left.val)
            if curr.right!=None:
                queue.append(curr.right)
                arr.append(curr.right.val)
        arr.sort()
        arr.append(1e09)
        for i in range(len(arr)-1):
            Min=min(Min,abs(arr[i+1]-arr[i]))
        return Min
if __name__ == "__main__":
    obj=Solution()
    arr1=[1,3,2,5]
    root1=build(arr1)
    M_root=obj.getMinimumDifference(root1)
    print(M_root) 