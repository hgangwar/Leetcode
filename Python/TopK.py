class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        Pf=dict()
        Nf=dict()
        for i in range(0,len(positive_feedback)):
            Pf[positive_feedback[i]]=0
        for i in range(0,len(negative_feedback)):
            Nf[negative_feedback[i]]=0
        Score=[0]*len(report)
        for i in range(0,len(report)):
            rep=report[i].split(' ')
            plus,minus=0,0
            for j in range(0,len(rep)):
                if rep[j] in Pf:
                    plus+=1
                if rep[j] in Nf:
                    minus+=1
            Score[i]=(3*plus)-minus
        ranking=dict()
        for i in range(0,len(Score)):
            if (Score[i] in ranking):
                ranking[Score[i]]+=[student_id[i]]
            else:
                ranking[Score[i]]=[student_id[i]]
        ranked=sorted(Score,reverse=True)
        l=len(ranked)-1
        ranked=[*set(ranked)]
        
        Op=[]
        for j in range(0,len(ranked)):
            key=ranked[j]
            stud=ranking[key]
            stud=sorted(stud)
            for x in stud:
                Op.append(x)
                if(len(Op)==k):
                    return Op
        return Op
        
if __name__ == "__main__":
    obj=Solution()
    positive_feedback=["smart","brilliant","studious"]
    negative_feedback=["not"]
    report=["this student is not studious","the student is smart"]
    student_id=[1,2]
    k=2
    Op=obj.topStudents(positive_feedback,negative_feedback,report,student_id,k)
    print(Op)
