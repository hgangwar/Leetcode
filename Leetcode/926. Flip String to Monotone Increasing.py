class Solution(object):
    def minFlipsMonoIncr(self, s):
        if(len(s)==1): return 0
        s=[int(i) for i in s]
        zeros,ones,count=[],[],0
        for i in range(len(s)):
            ones.append(count)
            if(s[i]==1): count+=1            
        count=0
        for i in range(len(s)-1,-1,-1):
            zeros.append(count)
            if(s[i]==0): count+=1            
        zeros=zeros[::-1]
        Min=[0]*len(s)
        for i in range(len(s)): Min[i]=zeros[i]+ones[i]  
        return min(Min)        

if __name__ == "__main__":
    obj=Solution()
    s = "11011"
    Op=obj.minFlipsMonoIncr(s)
    print(Op)