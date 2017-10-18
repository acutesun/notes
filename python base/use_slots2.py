from types import MethodType
def set_city(self,city):
    self.city = city
    
def set_country(self,country):
    self.country = country    

class Student(object):
    __slots__ = ('name','age','set_city') #限制student实例能添加的属性

c = Student()
d = Student()
 
c.set_city = MethodType(set_city,c) #将方法绑定在实例c上
c.set_city('china')
c.city
 
    
