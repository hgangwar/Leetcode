class Solution(object):
    def isAlienSorted(self, words, order):
        All=dict()
        for i,x in enumerate(order):
            All[x]=i
        if len(words)==1: return True
        for i in range(1,len(words)):
            x,y=words[i-1],words[i]
            n=min(len(x),len(y))
            if (x[:n]==y[:n] and len(x)>len(y)): return False
            for j in range(n):
                if (All[x[j]]==All[y[j]]): continue
                elif (All[x[j]]<All[y[j]]): break
                else:  return False            
        return True
if __name__ == "__main__":
    obj=Solution()
    Op=obj.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz")
    print(Op)