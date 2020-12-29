class python:
    def __init__(self,pages):
        self.pages=pages
    
    def __add__(self,other):
        return self.pages + other.pages
    
    def __gt__(self,other):
        return self.pages > other.pages
    
    def __sub__(self,other):
        return self.pages - other.pages
class sql:
    def __init__(self,pages):
         self.pages=pages
    
b1=python(123)
b2=sql(234)

print(b1+b2)
print(b1>b2)
print(b1-b2)