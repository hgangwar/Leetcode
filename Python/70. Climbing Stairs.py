import math
class Solution(object):
    def climbStairs(self, n):
        two,one=n//2,n%2
        ls=[2]*two+[1]*one
        size,Op=two+one,0        
        while(two>=0):
            N=math.factorial(size)
            p=math.factorial(two)
            q=math.factorial(one)
            Op+=(N)/(p*q)
            ls.pop(0)
            ls.append([1,1])
            size+=1
            two-=1
            one+=2            
        return int(Op)
if __name__ == "__main__":
    obj=Solution()
    Op=obj.climbStairs(2)
    print(Op)
