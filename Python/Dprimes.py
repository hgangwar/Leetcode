import math
class Solution(object):
    def getprime(self, num):
        ls=[]
        while(num%2==0):
            ls.append(2)
            num=int(num/2)
        for i in range(3, int(math.sqrt(num))+1, 2):
            if(num%i==0):
                while(num%i==0):
                    ls.append(i)
                    num=int(num/i)
        if(num>2):
            ls.append(num)
        return set(ls)
        
    def distinctPrimeFactors(self, nums):
        Dprimes=[]
        for x in nums:
            temp=list(self.getprime(x))
            Dprimes=set(list(Dprimes)+temp)
        return len(Dprimes)
if __name__ == "__main__":
    obj=Solution()
    Op=obj.distinctPrimeFactors([30])
    print(Op)
