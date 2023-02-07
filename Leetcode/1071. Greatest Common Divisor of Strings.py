class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1==str2: return str1    
        def common(s,t):
            if len(t)%len(s)!=0: return False
            i=0
            while(i<len(t)):
                if t[i:i+len(s)]!=s: return False
                i+=len(s)
            return True
        if (len(str1)<len(str2)):
            temp=str2
            str2=str1
            str1=temp
        hcf=str2        
        while hcf:
            T1=common(hcf,str2)
            T2=common(hcf,str1)
            if T1 and T2: return hcf
            L=len(hcf)-1
            while(len(str2)%L!=0 and L>1):
                L-=1
            if L==1: return ""
            hcf=hcf[:L]
        return ""
if __name__ == "__main__":
    obj=Solution()    
    Op=obj.gcdOfStrings("UETKZUETKZUETKZUETKZUETKZUETKZUETKZUETKZUETKZUETKZUETKZ", "UETKZUETKZUETKZUETKZUETKZUETKZUETKZUETKZUETKZUETKZUETKZUETKZUETKZ")
    print(Op)