# Author: Sam Brown
# Date: 23/3/2021
# Examples at the bottom
#to use:
#import MyMaths
#or
#from MyMaths import Polynomial, Term
import matplotlib.pyplot as plt


class Term:
    def __init__(self, coef, pow):
        self. coef = coef
        self. pow = pow

    def __mul__(self, other):
        if type(other) == Term:
            return Term(self.coef * other.coef, self.pow + other.pow)
        elif type(other) == int:
            return Term(self.coef * other, self.pow)

    def __add__(self, other):
        if self.pow == other.pow:
            return Term(self.coef + other.coef, self.pow)
        else:
            poly=Polynomial([self,other])
            return poly
        #else: return polynomial

    def __pow__(self, other):
        if type(other) == int:
            return Term(self.coef ** other, self.pow * other)
        #else: f**** you
    
    def __sub__(self, other):
        if self.pow == other.pow:
            return Term(self.coef + other. coef , self. pow)
        else:
            poly=Polynomial([self,other])
            return poly
        #else return polynomial

    def __truediv__(self, other):
        if type(other) == Term:
            return Term(self.coef / other.coef, self.pow-other.pow)

        elif type(other) == int:
            return Term(self.coef / other, self.pow)
    
    def __str__(self):
        term =""
        if self.coef == 1:
            term+=""

        else:
            term+=str(self.coef)

        if self.pow ==1:
            term+= "x"
        elif self.pow>1 or self.pow<0:
            term+= "x^"+ str (self.pow)
        
        return term
        

    def differentiate(self):
        return Term(self.coef * self.pow, self.pow-1)
    
    def integrate(self):
        return Term(self.coef/(self.pow+1), self.pow +1)
    
    def sub(self, x):
        if self.coef == 0:
            return 0
        if self.pow == 0:
            return self.coef
        return self.coef*x**self.pow






class Polynomial:
    def __init__(self, terms=[]):
        self.terms = terms

    def update(self, terms):
        for term in terms:
            self.terms.append(term)

    def __str__(self):
        string = str(self.terms[0])
        for ind in range(1,len(self.terms)):
            string+=" "
            if self.terms[ind].coef>0:
                string += "+"
            string+=str(self.terms[ind])
                
        return string
    

    def __pow__(self, other):
        poly = self
        if type(other) == int:
            for _n in range(other-1):
                poly=poly*self
        
        return poly


    def __add__(self, other):
        poly = Polynomial([])
        if type(other) == Polynomial:
            poly.update([term for term in self.terms])
            poly.update([term for term in other.terms])

        elif type(other) == Term:
            poly.update([term for term in self.terms])
            poly.update([other])
            
        poly.compress()
        return poly

    def __sub__(self, other):
        poly = Polynomial([])
        if type(other) == Polynomial:
            poly.update([term for term in self.terms])
            
            poly.update([term*-1 for term in other.terms])
            #poly.compress()

        elif type(other) == Term:
            poly.update([term for term in self.terms])
            poly.update([other*-1])
            poly.compress()

        return poly
    
    def __mul__(self, other):
        poly = Polynomial([])
        if type(other) == Polynomial:
            for term in self.terms:
                for anotherterm in other.terms:
                    newterm = term*anotherterm
                    poly.update([newterm])
            poly.compress()

        elif type(other) == Term:
            poly.update([term*other for term in self.terms])
                

        elif type(other) == int:
            poly.update([term*other for term in self.terms])
                
        return poly

    def __mod__(self,other):
        poly=Polynomial([])
        if type(other) == Polynomial:
            temp = self
            temp.sort()
            other.sort()
            index = 0
            while index<=len(other.terms):
                mult = temp.terms[index]/other.terms[0]
                newline = other*mult
                temp = temp-newline
                index+=1
            poly=temp
            poly.compress()
            #print(str(temp)+"/"+str(other))
        return poly

    def __floordiv__(self, other):
        poly = Polynomial([])
        if type(other) == int:
            poly.update([term/other for term in self.terms])

        elif type(other) == Term:
            poly.update([term/other for term in self.terms])

#This doesnt work fully for polynomials, WIP
#TODO Break this shit then fix again
        elif type(other) == Polynomial:
            temp = self
            temp.sort()
            other.sort()
            index = 0
            while index<=len(other.terms):
                mult = temp.terms[index]/other.terms[0]
                newline = other*mult
                temp = temp-newline
                poly.update([mult])
                index+=1
            poly.compress()
            #temp.compress()
            #print(str(temp)+"/"+str(other))
        return poly
# it works thats all u need to know there must be better ways
    def compress(self):
        compressed = False
        index = 0
        while not compressed and index<len(self.terms):
            found = False
            index2 = 0
            while not found and index2<len(self.terms):
                if index != index2:
                    if self.terms[index].pow == self.terms[index2].pow:
                        #yes this is really bad
                        self.terms[index]+= self.terms[index2]
                        del self.terms[index2]
                        index2-=1
                index2+=1
            index+=1
        index = 0
        #but it works
        while index<len(self.terms):
            if self.terms[index].coef == 0:
                del self.terms[index]
                index-=1
            index+=1

    def integrate(self):
        poly=Polynomial([term.integrate() for term in self.terms])
        return poly
    
    def differentiate(self):
        poly=Polynomial([term.differentiate() for term in self.terms])
        return poly
    
    def sub(self, x):
        ret = 0
        for term in self.terms:
            ret +=term.sub(x)
        return ret

    
    def sort(self):
        self.terms = sorted(self.terms, key= lambda item: item.pow , reverse = True)
        
    @staticmethod
    def parser(get_input):
        input_str = get_input.split("+")
        terms = []
        for term in input_str:
            has_x = False
            has_pow = False
            for chara in term:
                if chara =='^':
                    has_pow = True
                elif chara == 'x':
                    has_x = True
            
            if has_x:
                cursor = 0
                while term[cursor] != 'x':
                    cursor+=1
                if cursor ==0:
                    coef = 1
                else:
                    coef = float(term[:cursor])
            else:
                coef = float(term)

            if has_pow:
                cursor = len(term)-1
                while term[cursor] != '^':
                    cursor-=1
                pow = float(term[cursor+1:])

            elif has_x and not has_pow:
                pow = 1

            elif not has_x and not has_pow:
                pow = 0

            terms.append(Term(coef, pow))
        return terms
    
    def plot(self, a, b):
        datax =[]
        datay =[]
        x=a
        while x<=b:
            datax.append(x)
            datay.append(self.sub(x))
            x+=0.01
        plt.plot(datax, datay, label = str(self))
        
        
        
# not too great code but it works pretty well

    

class Matrix:
    def __init__(self, dim):
        self.dim = dim
        self.matrix = list([0 for n in range (0, self.dim[1])] for m in range(0, self.dim[0]))
        
   
    def update_row(self, row, num):
        self.matrix[num]=row

    def update_column(self, column,num):
        for n in range(0,self.dim[0]):
            self.matrix[n][num]=column[n]

    def update_matrix(self, matrix):
        if self.dim[0] == len(matrix) and self.dim[1] == len(matrix[0]):
            self.matrix = matrix


    def __mul__(self, other):
        if self.dim[1] == other.dim[0]:
            temp = Matrix([self.dim[0], other.dim[1]])
            for i in range(self.dim[0]):
   # iterate through columns of Y
                for j in range(other.dim[1]):
                    # iterate through rows of Y
                    for k in range(other.dim[0]):
                        temp.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return temp
        else:
            print("LOL, that dont work!")
    
    
    def __add__(self, other):
        temp = Matrix(self.dim)
        if self.dim == other.dim:
            for m in range(self.dim[0]):
                for n in range(self.dim[1]):
                    temp.matrix[n][m] = self.matrix[n][m] + other.matrix[n][m]
        return temp
    
    def __sub__(self, other):
        temp = Matrix(self.dim)
        if self.dim == other.dim:
            for m in range(self.dim[0]):
                for n in range(self.dim[1]):
                    temp.matrix[n][m] = self.matrix[n][m] - other.matrix[n][m]
        return temp

    def __str__(self):
        string = ""
        for n in range(0, self.dim[0]):
            string+=str(self.matrix[n])+"\n"
            
        return string

    

if __name__ == "__main__":
    a = Polynomial([]).parser("6x+-1x^2")
    #f.plot(-100,100)
    #plt.show()
    A = Matrix([2,2])
    A.update_row([1,2], 0)
    A.update_row([2,3],1)
    print(A)
    B = Matrix([2,2])
    B.update_row([4,5],0)
    B.update_row([1,1],1)
    B.update_column([1,2], 1)
    print(B)
    C = A * B
    print(C)
    

    #b.plot(-10,10)
    #print(c)
    #c.plot(10,100)
    #c.compress()
    #print(c)
    #c.plot(10,100)

    #a.plot(10,100)
    #a.plot(-10,10)
   # plt.show()