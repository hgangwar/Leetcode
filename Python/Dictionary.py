class Solution(object):
    def twoSum(self, numbers, target):
        l=len(numbers)
        D=dict()
        type(D)
        for i in range(0,l):
            D[numbers[i]]=i
        for x in D:
            y=target-x
            if ( y in D and D[x]!=D[y]):
                return [min(D[x]+1,D[y]+1), max(D[x]+1,D[y]+1)]
            if (2*x==target):
                if D[x]!=l-1:
                    if numbers[D[x]+1]==numbers[D[x]]:
                        return [D[x],D[x]+1]
                if D[x]!=0:
                    if numbers[D[x]-1]==numbers[D[x]]:
                        return [D[x]-1,D[x]]
if __name__ == "__main__":
    obj=Solution()
    Op=obj.twoSum([0,0,3,4],0)
    print(Op)