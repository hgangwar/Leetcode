class Solution:
    def reverseBits(self, n):
        Op,powe=0,31
        while(n):
            Op+=(n&1)<<powe
            n=n>>1
            powe-=1
        return Op
if __name__ == "__main__":
    obj=Solution()
    n =int("00000010100101000001111010011100",2)
    print(n)
    Op=obj.reverseBits(n)
    print(Op)
