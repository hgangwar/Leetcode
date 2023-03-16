class Solution(object):
    def totalFruit(self, fruits):
        count,Maxcount,lastX=0,0,1
        basket,ndx=set(),0
        while(ndx<len(fruits)):
            if len(basket)<2:
                basket.add(fruits[ndx])
            elif not fruits[ndx] in basket:
                Maxcount=max(count,Maxcount)
                count=ndx-lastX
                basket={fruits[ndx-1],fruits[ndx]}
            if fruits[ndx]!=fruits[ndx-1]:
                lastX=ndx
            count+=1
            ndx+=1   
        return max(Maxcount,count)
if __name__ == "__main__":
    obj=Solution()
    Op=obj.totalFruit([1,2,3,2,2])
    print(Op)