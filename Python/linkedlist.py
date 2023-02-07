
class Solution(object):
    def printLl(self, head):
        l=[]
        while(head!=None):
            l.append(head.data)
            head=head.next
        print(l)
    def middleNode(self, head):
        slow,fast=head,head
        temp=slow.data
        while(fast!=None and fast.next!=None ):
            slow=slow.next
            fast=fast.next.next
        return slow
    def reverseList(self, head):
        self.printLl(head)
        while(head.next!=None):
            temp=head.next
            show=head.data
            show2=temp.data
            head=temp 
            temp.next=head                       
        return head
class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class SLinkedList:
   def __init__(self):
      self.headval = None
if __name__ == "__main__":
    obj=Solution()
    arr=[1,2,3,4,5]
    head=Node(arr[0]) 
    real_head=head
    for i in range(1,len(arr)):
        head.next=Node(arr[i])
        head=head.next    
    Op=obj.reverseList(real_head)
    l=[]
    while(Op.next!=None):
        l.append(Op.data)
        Op=Op.next
    print(l)
