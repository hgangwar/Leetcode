class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.value=value
        self.ls=[]
        self.size=k
        self.count=0
    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num!=self.value):            
            self.count=0
        else:
            self.count+=1
        #print(self.ls,self.size,self.count)
        self.ls.append(num)
        if(self.count>=self.size):
            return True
        else:
            return False
if __name__ == "__main__":
    value,k=4,3
    obj = DataStream(value, k)
    param_1 = obj.consec(4)
    print(param_1)
    param_1 = obj.consec(4)
    print(param_1)
    param_1 = obj.consec(4)
    print(param_1)
    param_1 = obj.consec(3)
    print(param_1)