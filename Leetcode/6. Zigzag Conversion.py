class Solution(object):
    def convert(self, s, Rows):
        ls,ndx=[""]*Rows,0
        while(ndx<len(s)):
            j=0
            while j<Rows and ndx<len(s):
                ls[j]=ls[j]+s[ndx]
                j+=1
                ndx+=1
            j-=2
            while j>0 and ndx<len(s):
                ls[j]=ls[j]+s[ndx]
                j-=1
                ndx+=1
        ls="".join(ls)
        return ls
if __name__ == "__main__":
    obj=Solution()
    Op=obj.convert("PAYPALISHIRING",3)
    print(Op)