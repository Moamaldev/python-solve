class StringOperations(): 

    def __init__(self, string): 
        self.string = string 


    def reverse(self):
        print("Reverse :",self.string[::-1])

class ReversedString(StringOperations): 

    def Get(self): 
        return self

a=input("Enter String: ")
s= ReversedString(a)
print("Enterd : ",a)
s.reverse()
