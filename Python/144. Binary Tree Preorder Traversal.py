from binarytree import build
class Solution(object):
    def preorderTraversal(self, root):
        queue=[]
        queue.append(root)
        ndx=0
        while(ndx<len(queue)):
            root=queue[ndx]
            if(root!=None):
                if(root.left!=None):
                    queue.insert(ndx+1,root.left)
                if(root.right!=None and root.left!=None ):
                    queue.insert(ndx+2,root.right)
                if(root.right!=None and root.left==None):
                    queue.insert(ndx+1,root.right)
            ndx+=1            
        ls=[]
        for x in queue:
            if(x!=None):
                ls.append(x.value)
        return ls
if __name__ == "__main__":
    obj=Solution()
    arr=[2,1,3,None,4]
    root=build(arr)
    print(root)
    Op=obj.preorderTraversal(root)
    print(Op)
