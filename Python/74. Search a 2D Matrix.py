class Solution(object):
    def searchMatrix(self, matrix, target):
        start,end,Start=0,len(matrix)-1,0
        while(start<end+1):
            mid=int((start+end)//2)
            if(matrix[mid][0]==target):
                return True
            if(matrix[mid][0]>target):
                end=mid-1
            elif(matrix[mid][0]<target):
                start=mid+1
        if(start<len(matrix)):
            if(matrix[start][0]<=target and matrix[start][-1]>=target):
                Start=start
        if(end>=0):
            if(matrix[end][0]<=target and matrix[end][-1]>=target):
                Start=end
        else:
            return False
        start,end=0,len(matrix[0])-1
        while(start<=end):
            mid=int((start+end)//2)
            if(matrix[Start][mid]==target):
                return True
            if(matrix[Start][mid]>target):
                end=mid-1
            elif(matrix[Start][mid]<target):
                start=mid+1
        return False
        
if __name__ == "__main__":
    obj=Solution()
    matrix = [[1]]
    target = 2
    Op=obj.searchMatrix(matrix,target)
    print(Op)

