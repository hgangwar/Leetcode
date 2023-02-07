from itertools import product
class Solution(object):
    def restoreIpAddresses(self, s):
        n,res=len(s),[]
        Comb=list(product([1, 2, 3], repeat=4))
        i=0
        while(i<len(Comb)):
            x=Comb[i]
            if sum(x)!=n:
                Comb.pop(i)
            else: i+=1
        for x in Comb:
            [i,j,k,l]=[x[0],x[0]+x[1],x[0]+x[1]+x[2],sum(x)]
            a,b,c,d=int(s[0:i]),int(s[i:j]),int(s[j:k]),int(s[k:l])
            if(a<256 and b<256 and c<256 and d<256):
               if (int(s[0])!=0 or x[0]==1) and (int(s[i])!=0 or x[1]==1) and (int(s[j])!=0 or x[2]==1) and (int(s[k])!=0 or x[3]==1):
                    res.append(str(a)+"."+str(b)+"."+str(c)+"."+str(d))
                    print([a,b,c,d])
        return res
if __name__ == "__main__":
    obj=Solution()
    Op=obj.restoreIpAddresses("101023")
    print(Op)