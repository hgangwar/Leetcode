class Solution(object):
    def findMinArrowShots(self, points):
        points = sorted(points, key = lambda x:x[1])
        Arrow, Ans,n=[0]*2, 1, len(points)
        i=0
        Arrow[0]=points[0][0]
        Arrow[1]=points[0][1]
        while(i<n):
            while(i<n):
                if(Arrow[0]==points[i][0]):
                    i+=1
                else:
                    break
            if(i==n):
                break
            if(Arrow[1]<points[i][0] and Arrow[1]<points[i][1]):
                Ans+=1
                Arrow[0]=points[i][0]
                Arrow[1]=points[i][1]
            elif (Arrow[1]>points[i][1]):
                Arrow[0]=points[i][0]
                Arrow[1]=points[i][1]
            else:
                Arrow[0]=points[i][0]
        Ans+=1
        return Ans
if __name__ == "__main__":
    obj=Solution()
    points = [[8,9],[2,11],[3,12],[0,8],[8,13],[0,9],[6,9],[8,13],[6,7],[1,6]]
    Op=obj.findMinArrowShots(points)
    print(Op)

"""
[[8,9],[2,11],[3,12],[0,8],[8,13],[0,9],[6,9],[8,13],[6,7],[1,6]]
"""