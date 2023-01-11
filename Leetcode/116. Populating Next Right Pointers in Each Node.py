import math
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):    
    def connect(self, root):
        if root is None or root.left is None:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
        
if __name__ == "__main__":
    obj=Solution()
    #arr=[1,2,3,4,5,6,7]
    arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    height=math.log2(len(arr)+1)
    root=Node(arr[0])
    def build(root,level,index):
        if(2**level+index<=len(arr)):
            root.left=Node(arr[index])
            root.right=Node(arr[index+1])
            root.left=build(root.left,level+1,index+2)
            root.right=build(root.right,level+1,index+3)
        return root
    root=build(root,1,1)    
    M_root=obj.connect(root)    
    print(M_root)
    
    """ BFS soln
    class Solution(object):
    def connect(self, root):
        if not root:
            return root
        
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root
        
        # Once we reach the final level, we are done
        while leftmost.left:
            
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                
                # Progress along the list (nodes on the current level)
                head = head.next
            
            # Move onto the next level
            leftmost = leftmost.left
     """