from heapq import heappop, heappush, heapify
class Solution(object):
    def minStoneSum(self, piles, k):        
        heap=[]
        heapify(heap)
        for x in piles:
            heappush(heap,-x)
        print(heap)
        while(k>0):
            if(heap[0]%2==0):
                temp=int(heap[0]/2)
            else:
                temp=int((heap[0])//2)
            heappush(heap, temp)
            heappop(heap)
            k-=1
        piles=list(heap)
        return -sum(piles)

if __name__ == "__main__":
    obj=Solution()
    piles =[5,4,6,6,6,6,6,9]
    k = 2
    Op=obj.minStoneSum(piles,k)
    print(Op)

