class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        Head=head
        Prev=ListNode(-101,head)
        PPrev=ListNode(-101,Prev)
        while(head!=None):
            if(Prev.val!=head.val):
                PPrev=Prev
                Prev=head
                head=head.next
            else:
                while(head!=None): 
                    if(head.val!=Prev.val):
                        break
                    else:
                        head=head.next
                Prev=head
                PPrev.next=Prev
                if(head!=None):
                    head=head.next
        return Head
if __name__ == "__main__":
    obj=Solution()
    arr=[1,2,3,3,4,4,5]
    head=ListNode(arr[0]) 
    real_head=head
    for i in range(1,len(arr)):
        head.next=ListNode(arr[i])
        head=head.next
    Op=obj.deleteDuplicates(real_head)
    l=[]
    while(Op!=None):
        l.append(Op.val)
        Op=Op.next
    print(l)
