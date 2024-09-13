class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    
    def computeDifference(self):
        max_num = self.__elements[0]
        min_num = self.__elements[0]
        for e in self.__elements:
            if max_num < e:
                max_num = e
            if min_num > e:
                min_num = e
            # print(max_num, min_num)
        self.maximumDifference = max_num - min_num
        return
            
        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)