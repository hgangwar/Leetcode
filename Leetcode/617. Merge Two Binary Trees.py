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