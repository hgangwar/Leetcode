class SummaryRanges(object):
    def __init__(self):
        self.arr=set()
        return
    def addNum(self, value):
        self.arr.add(value)
        return
    def getIntervals(self):
        nums=list(self.arr)
        nums.sort
        intervals=[]
        i,flag=0,True
        nums.append(-3)
        while(i<len(nums)-1):
            if flag: 
                front=nums[i]
                flag=False
            if (nums[i]!=nums[i+1]-1):
                if nums[i]==nums[i+1]-1:
                    end=nums[i+1]
                else: end=nums[i]
                intervals.append([front,end])
                flag=True
            i+=1
        nums.pop(-1)
        return intervals
if __name__ == "__main__":
    obj = SummaryRanges()
    commands=["addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]
    nums=[[49],[],[97],[],[53],[],[5],[],[33],[],[65],[],[62],[],[51],[],[100],[],[38],[],[61],[],[45],[],[74],[],[27],[],[64],[],[17],[],[36],[],[17],[],[96],[],[12],[],[79],[],[32],[],[68],[],[90],[],[77],[],[18],[],[39],[],[12],[],[93],[],[9],[],[87],[],[42],[],[60],[],[71],[],[12],[],[45],[],[55],[],[40],[],[78],[],[81],[],[26],[],[70],[],[61],[],[56],[],[66],[],[33],[],[7],[],[70],[],[1],[],[11],[],[92],[],[51],[],[90],[],[100],[],[85],[],[80],[],[0],[],[78],[],[63],[],[42],[],[31],[],[93],[],[41],[],[90],[],[8],[],[24],[],[72],[],[28],[],[30],[],[18],[],[69],[],[57],[],[11],[],[10],[],[40],[],[65],[],[62],[],[13],[],[38],[],[70],[],[37],[],[90],[],[15],[],[70],[],[42],[],[69],[],[26],[],[77],[],[70],[],[75],[],[36],[],[56],[],[11],[],[76],[],[49],[],[40],[],[73],[],[30],[],[37],[],[23],[]]
    for i,x in enumerate(commands):
        if x=="addNum":
            eval("obj."+x+"("+str(nums[i][0])+")")
        else:
            eval("print(obj."+x+"())")