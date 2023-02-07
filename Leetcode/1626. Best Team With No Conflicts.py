class Solution(object):
    def bestTeamScore(self, scores, ages):
        for i in range(len(scores)):
            ages[i]=[ages[i], scores[i]]
        ages.sort(reverse=True)
        n=len(ages)
        ans,i=[0]*n,0
        ages.append([0,0])
        while(i<n):
            j=i-1
            while (j>=0):
                if ages[i][1]<=ages[j][1] or ages[i]==ages[j]:
                    ans[i]=max(ans[i],ages[i][1]+ans[j])
                j-=1
            if ans[i]==0: ans[i]=ages[i][1]
            i+=1            
        return max(ans)
if __name__ == "__main__":
    obj=Solution()
    Op=obj.bestTeamScore([596,277,897,622,500,299,34,536,797,32,264,948,645,537,83,589,770],[18,52,60,79,72,28,81,33,96,15,18,5,17,96,57,72,72])
    print(Op)