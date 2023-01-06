from itertools import product
class Solution(object):
    def calcEquation(self, equations, values, queries): 
        Map=dict()
        Sym=dict()
        Nodes=dict()
        """ Dictionary"""
        for i in range(0,len(equations)):
            x=tuple(equations[i])
            Sym[x[0]]=0
            Sym[x[1]]=0
            if(x[0]==x[1] or x[0]==x[1][::-1]):
                continue            
            Map[x]=values[i]
            if(not x[0] in Nodes):
                Nodes[x[0]]=[x[1],values[i]]
            else:
                Nodes[x[0]]=Nodes[x[0]]+[x[1],values[i]]
            Map[x[::-1]]=1/values[i]
            if(not x[1] in Nodes):
                Nodes[x[1]]=[x[0],1/values[i]]
            else:
                Nodes[x[1]]+=[x[0],1/values[i]]
            if(len(x[0])==2  and len(x[1])==1): 
                x1=list(x[0][::1])

            if(len(x[0])==2  and len(x[1])==2):
                x1=list(x[0][::1])
                x2=list(x[1][::1])
                mini=list(product(x1,x2))
                flag,j=0,0
                switch=[3,2,1,0]
                while(j<4 and flag==0):
                    y=tuple(mini[j])
                    if y in Map:
                                z=mini[switch[j]]
                                Map[z]=values[i]/Map[y]
                                if(not z[0] in Nodes):
                                    Nodes[z[0]]=[z[1],values[i]/Map[y]]
                                else:
                                    Nodes[z[0]]+=[z[1],values[i]/Map[y]]
                                
                                Map[z[::-1]]=Map[y]/values[i]
                                if(not z[1] in Nodes):
                                    Nodes[z[1]]=[z[0],Map[y]/values[i]]
                                else:
                                    Nodes[z[1]]+=[z[0],Map[y]/values[i]]                                
                                flag=1
                                Sym[z[0]]=0
                                Sym[z[1]]=0
                                break
                    j+=1
        
        """ Queries"""
        Op=[-1]*len(queries)        
        for i in range(0,len(queries)):
            x=tuple(queries[i])
            if ((x[0]==x[1] or x[0]==x[1][::-1]) and x[0] in Sym and x[1] in Sym ):
                Op[i]=1
            elif (len(x[0])==1 and x[0] in Sym and x[1] in Sym):
                path=self.find_path(Nodes,x[0],x[1],[])                
                if(path):
                    Op[i]=self.value(Map,path)
                
            elif (len(x[0])==2):

                x1=list(x[0][::1])
                x2=list(x[1][::1])
                mini=list(product(x1,x2))
                flag,j=0,0
                while(j<4 and flag==0):
                    y=tuple(mini[j])
                    path=self.find_path(Nodes,y[0],y[1],[])
                    if(path==None):
                        j+=1
                        continue
                    val1=self.value(Map,path)
                    for z in mini:
                        if set(y).isdisjoint(set(z)):
                            path=self.find_path(Nodes,z[0],z[1],[])
                            if (path==None):
                                continue
                            val2=self.value(Map,path)
                            Op[i]=val1*val2
                            flag=1
                    j+=1
                
        return Op
    def find_path(self, Nodes,start,end,path=[]):
        path=path+[start[0]]        
        if(start[0]==end[0]):
            return path        
        if not start[0] in Nodes:
            return None
            
        for i in range(0,int(len(Nodes[start])/2)):
            temp=(Nodes[start])
            node=Nodes[start][2*i]
            if node not in path:
                newpath = self.find_path(Nodes, node[0], end, path)
                if newpath: return newpath
            
        return None
            
    def value(self,Map , path):
        i,val=0,1
        while(i<len(path)-1):
            key=tuple([path[i],path[i+1]])
            val=val*Map[key]
            i+=1
        return val


if __name__ == "__main__":
    obj=Solution()
    equations =[["a","aa"]]
    values =    [9.0]
    queries =[["aa","a"],["aa","aa"]]

    Op=obj.calcEquation(equations,values,queries)
    print(Op)