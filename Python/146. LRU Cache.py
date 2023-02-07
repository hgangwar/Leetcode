from collections import defaultdict
class LRUCache(object):
    def __init__(self, capacity):
        self.Value=defaultdict(int)
        self.stack=[]
        self.size=capacity
        return
    def get(self, key):
        if key in self.Value:
            self.stack.remove(key)
            self.stack.append(key)
            return self.Value[key]
        return -1
    def put(self, key, value):
        if self.size==0: return
        if len(self.Value)==self.size and key not in self.Value:
            rem=self.stack.pop(0)
            self.Value.pop(rem)
        elif key in self.Value:
            self.stack.remove(key)
        self.Value[key]=value
        self.stack.append(key)
        return
if __name__ == "__main__":
    commands=["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    nums=[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    for i,x in enumerate(commands):
        if x=="LRUCache":
            obj=LRUCache(nums[i][0])
        elif x=="put":
            eval("obj."+x+"("+str(nums[i][0])+","+str(nums[i][1])+")")
        else:
            eval("print(obj."+x+"("+str(nums[i][0])+"))")