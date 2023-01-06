 
class Node(object):
     def __init__(self, data=0, next=None):
         self.data = data
         self.next = next
class Solution(object):
    def printLl(self, head):
        l=[]
        while(head!=None):
            l.append(head.data)
            head=head.next
        print(l)
    def reverseList(self, head):
        self.printLl(head)
        Prev=None
        while(head!=None):
            temp=head.next
            head.next=Prev
            Prev=head
            head=temp                       
        return Prev
    def removeNthFromEnd(self, head, n):
        dummy = Node(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:

            right = right.next
            left = left.next

        left.next = left.next.next
        #self.printLl(dummy.next)
        return dummy.next
        
        #return head
if __name__ == "__main__":
    obj=Solution()
    arr=[1,2,3,4,5]
    head=Node(arr[0]) 
    real_head=head
    for i in range(1,len(arr)):
        head.next=Node(arr[i])
        head=head.next
    #Op=obj.removeNthFromEnd(real_head,2)
    Op=obj.reverseList(real_head)
    #temp=Op.next
    l=[]
    while(Op!=None):
        l.append(Op.data)
        Op=Op.next
    print(l)