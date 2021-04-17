import math


class IsSumName:
    my_dict = {1: "a,j,s", 2: "b,k,t", 3: "c,i,u", 4: "d,m,v", 5: "e,n,w",
               6: "f,o,x", 7: "g,p,y", 8: "h,q,z", 9: "i,r"}

    def __init__(self):
        self.name = input("Please input name: ")
        self.sum_ = 0
        for i in range(len(self.name)):
            if self.name[i] in self.my_dict[i + 1]:
                self.sum_ = i + 1
        if math.sqrt(self.sum_) > 5:
            print("yes")
        else:
            print("No")


IsSumName()