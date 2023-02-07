import math
class Solution(object):
    def pickGifts(self, gifts, k):
        for i in range(k):
            gifts.sort()
            gifts[-1]=int(math.sqrt(gifts[-1]))
        return int(sum(gifts))
            
if __name__ == "__main__":
    obj=Solution()
    Op=obj.pickGifts([54,6,34,66,63,52,39,62,46,75,28,65,18,37,18,13,33,69,19,40,13,10,43,61,72],7)
    print(Op)