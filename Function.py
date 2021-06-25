from MyMaths import Polynomial, Term
import matplotlib.pyplot as plt

class Function(Polynomial):
    def __init__(self,  range, terms = []):
        super().__init__(terms)
        self.range = range
    
    def isinrange(self, x):
        if x>=self.range[0] and x<=self.range[1]:
            return True
        else:
            return False
    
    def sub(self, x):
        if self.isinrange:
            ret = 0
            for term in self.terms:
                ret +=term.sub(x)
            return ret
        
        else:
            return 0
    
    def overlaps(self, other):
        if self.range[1] - other.range[0] <0:
            return True
        
        return False

    

class ListOfFunctions:
    def __init__(self):
        self.functions = []
    
    def addfunction(self, function):
        #check if range overlaps
        overlap = False
        for afunction in self.functions:
            if function.overlaps(afunction):
                overlap = True
        
        if not overlap:
            self.functions.append(function)
    
    def sub(self, x):
        for afunction in self.functions:
            if afunction.isinrange(x):
                return afunction.sub(x)

        raise ValueError('Input Not In Range')

    def plot(self, a, b):
        datax =[]
        datay =[]
        x=a
        while x<=b:
            datax.append(x)
            datay.append(self.sub(x))
            x+=0.01
        plt.plot(datax, datay, label = str(self))
    
    def findlocalmax(self, x):
        if self.sub(x+1)>self.sub(x) and self.sub(x-1)<self.sub(x):
            return self.findlocalmax(x+1)
        if self.sub(x+1)<self.sub(x) and self.sub(x-1)>self.sub(x):
            return self.findlocalmax(x-1)
        if self.sub(x+1)<=self.sub(x) and self.sub(x-1)<=self.sub(x):
            return x
        

        
        





if __name__ == "__main__":
    alist = ListOfFunctions()
    poly = Polynomial(Polynomial.parser("2x^2+5x+-240"))
    
    alist.addfunction(Function((0, 10), Polynomial.parser("2x^2+5x+-240")))
    alist.addfunction(Function((10,15), Polynomial.parser("x")))
    alist.addfunction(Function((15,22), Polynomial.parser("x^2+-210")))
    alist.plot(0,22)

    plt.show()

    

        
            

        
    
            

        
