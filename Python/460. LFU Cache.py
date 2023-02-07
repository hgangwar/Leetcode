from collections import defaultdict
class LFUCache(object):
    def __init__(self, capacity):
        self.used=defaultdict(int)
        self.Value=defaultdict(int)
        self.stack=defaultdict(list)
        self.size=capacity
        return
    def get(self, key):
        if key in self.Value:
            self.stack[self.used[key]].remove(key)
            self.used[key]+=1
            self.stack[self.used[key]].append(key)
            return self.Value[key]
        return -1

    def put(self, key, value):
        if self.size==0: return
        if len(self.Value)==self.size and key not in self.Value:
            Min_use=1
            while(not self.stack[Min_use]):
                Min_use+=1
            lru=self.stack[Min_use].pop(0)
            self.Value.pop(lru)
            self.used.pop(lru)            
        elif key in self.Value:
            self.stack[self.used[key]].remove(key)            
        self.used[key]+=1
        self.Value[key]=value
        self.stack[self.used[key]].append(key)
        return
if __name__ == "__main__":

    commands=["LFUCache","put","get"]
    nums=[[0],[0,0],[0]]
    for i,x in enumerate(commands):
        if x=="LFUCache":
            obj=LFUCache(nums[i][0])
        elif x=="put":
            eval("obj."+x+"("+str(nums[i][0])+","+str(nums[i][1])+")")
        else:
            eval("print(obj."+x+"("+str(nums[i][0])+"))")