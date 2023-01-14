class Solution(object):
    def minimumPartition(self, s, k):
        n=len(str(k))
        l=len(s)-1
        curr,ndx,count=n,0,0
        if(n>=l+1):
            if(int(s)<=k):return 1
        while (curr>0):
            if(int(s[ndx:curr+ndx])<=k):
                ndx=ndx+curr
                count+=1
            else:
                if(curr>1):
                    ndx=ndx+curr-1
                    count+=1
                else:
                    return -1
            if(ndx+curr>l):
                if(int(s[ndx:l+1])<=k):
                    return count+1
        return count
if __name__ == "__main__":
    obj=Solution()
    s = "2433594"
    k = 1019944
    Op=obj.minimumPartition(s,k)
    print(Op)
