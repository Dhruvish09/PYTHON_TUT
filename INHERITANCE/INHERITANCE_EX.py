class polygon:
    __width=None
    __height=None
    
    def set_value(self,width,height):
        self.__width=width
        self.__height= height
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
        
class square(polygon):
    def area(self):
        return self.get_width()*self.get_height()
    
class triangle(polygon):
    def area(self):
        return self.get_width()*self.get_height()*1/2
        
    
s1=square()
s1.set_value(8,15)
print(s1.area())

t1=triangle()
t1.set_value(5,10)
print(t1.area())
        