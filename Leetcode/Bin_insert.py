class Solution(object):
    def addNum(self, value,arr):
            start,end=0,len(arr)-1
            mid=0
            while(start<end):
                mid=(start+end)//2
                if (value==arr[mid]): return
                if (value>arr[mid]):
                    start=mid+1
                else:
                    end=mid-1
            mid=(start+end)//2
            if not arr: return [value]
            if value<arr[mid]: arr.insert(mid,value)
            else : arr.insert(mid+1,value)
            return arr
if __name__ == "__main__":
    obj=Solution()
    Op=obj.addNum(1,[])
    Op=obj.addNum(3,Op)
    Op=obj.addNum(7,Op)
    Op=obj.addNum(2,Op)
    Op=obj.addNum(6,Op)
    print(Op)