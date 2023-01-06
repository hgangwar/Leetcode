from binarytree import build
class Solution(object):
    def mergeTrees(self, root1, root2):        
        if(root1==None and root2!=None):
            root1=root2
            return root1            
        elif(root1!=None and root2!=None):
            root1.value+=root2.value
        elif(root2==None):
            return root1
        root1.left=self.mergeTrees(root1.left,root2.left)
        root1.right=self.mergeTrees(root1.right,root2.right)        
        return root1

if __name__ == "__main__":
    obj=Solution()
    arr1=[1,3,2,5]
    arr2=[2,1,3,None,4,None,7]
    root1=build(arr1)
    root2=build(arr2)
    M_root=obj.mergeTrees(root1, root2)
    print(M_root)



    """
    level,index=0,1
    def createTree(root,arr,level,index):
        if (len(arr)>index):
            root.left=TreeNode(arr[index])
        createTree(root.left,level+1,index+(2**level))
        if (len(arr)>index+1):
            root.right=TreeNode(arr[index+1])        
        createTree(root.right,level+1,index+(2**level))
    createTree(root,arr,level,index)
       
    temp=obj.traverseTree(real_root,[])
    print(temp)

    def traverseTree(self, root,arr=[]):
        arr.append(root.val)
        if(root.left!=None):
            arr.append(root.left.val)
        if(root.right!=None):
            arr.append(root.right.val)
        if(root.left!=None):
            arr=self.traverseTree(root.left,arr)
        if(root.right!=None):
            arr=self.traverseTree(root.left,arr)
        return arr
    """