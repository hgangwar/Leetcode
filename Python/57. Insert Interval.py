class Solution(object):
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        if(newInterval[0]>intervals[-1][1]):
            intervals.append(newInterval)
            return intervals
        n=max(intervals[-1][1],newInterval[1])+1
        back,pos,gap=-1,0,-1
        for i,x in enumerate(intervals):
            if(gap<newInterval[0]<x[0]) and ((gap<newInterval[1]<x[0])):
                intervals.insert(i,newInterval)
                return intervals
            elif(x[0]<=newInterval[0]<=x[1]) and x[0]<=newInterval[1]<=x[1]:
                return intervals
            elif(back<=newInterval[0]<=x[1]):
                pos=i
                intervals[i][0]=min(intervals[i][0],newInterval[0])
                intervals[i][1]=max(newInterval[1],intervals[i][1])
                break
            back=x[0]
            gap=x[1]
        i=pos
        while(i<len(intervals)-1):
            if(intervals[pos][1]<intervals[i+1][0]):
                break
            i+=1
        intervals[pos][1]=max(intervals[i][1],intervals[pos][1])
        intervals=intervals[:pos+1]+intervals[i+1:]
        return intervals
if __name__ == "__main__":
    obj=Solution()
    intervals = [[1,5]]
    newInterval = [0,1]
    Op=obj.insert(intervals, newInterval)
    print(Op)