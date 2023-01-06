class Solution(object):
    def closetTarget(self, words, target, startIndex):
        n,left,right=len(words),startIndex,startIndex
        kleft,kright,flag=0,0,0
        while(kleft<=int(n/2)+1):
            if(words[left]==target):
                flag=1
                break
            left-=1
            kleft+=1
            if(left==-1):
                left=n-1
        while(kright<=int(n/2)+1):
            if(words[right]==target):
                flag=1
                break
            right+=1
            kright+=1
            if(right==n):
                right=0
        if flag!=1:
            return -1
        else:
            return min(kleft, kright)
if __name__ == "__main__":
    obj=Solution()
    words = ["hello","i","am","leetcode","hello"]
    target = "hello"
    startIndex = 1
    Op=obj.closetTarget(words,target,startIndex)
    print(Op)
