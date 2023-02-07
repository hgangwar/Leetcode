from heapq import heappop, heappush, heapify
class Solution(object):
    def getOrder(self, tasks):
        n,  seq=len(tasks), []
        tasks=[tasks[i]+[i] for i in range(n)]
        tasks.sort(key=lambda row:(row[0]))
        heap=[]
        heapify(heap)
        time=tasks[0][0]
        i,t=0,0
        while(i<n):            
            while(t<n):
                if not (time>=tasks[t][0]):
                    break
                x=tasks[t]
                y=[x[1],x[2]]
                heappush(heap,y)
                t+=1    
            if not (heap):
                time=tasks[t][0]
                continue
            y=heap[0]
            time+=y[0]
            seq.append(y[1])
            heappop(heap)
            i=t
        left=n-len(seq)
        for i in range(left): 
            temp=heap[0]
            seq.append(temp[1])
            heappop(heap)
        return seq

if __name__ == "__main__":
    obj=Solution()
    tasks = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]
    Op=obj.getOrder(tasks)
    print(Op)
