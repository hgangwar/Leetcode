from collections import defaultdict
class FreqStack(object):
    def __init__(self):
        self.stack=defaultdict(list)
        self.freq=defaultdict(int)
        self.Max_key=0
    
    def push(self, val):
        self.freq[val]+=1
        self.stack[self.freq[val]].append([val])
        if self.Max_key<self.freq[val]:
            self.Max_key=self.freq[val]
        return
    def pop(self):
        ans=self.stack[self.Max_key].pop(-1)[0]
        self.freq[ans]-=1
        while not self.stack[self.Max_key]:
            self.Max_key-=1
            if self.Max_key==0:  break
        return ans
if __name__ == "__main__":
    commands=["FreqStack","push","push","push","push","pop", "pop", "push", "push", "push", "pop", "pop", "pop"]
    nums=[[],[1], [1], [1], [2], [], [], [2], [2], [1], [], [], []]
    for i,x in enumerate(commands):
        if x=="FreqStack":
            obj=FreqStack()
        elif x=="push":
            eval("obj."+x+"("+str(nums[i][0])+")")
        else:
            eval("print(obj."+x+"())")