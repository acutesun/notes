class Student(object):
    def __init__(self,name):
        self.name = name
  
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        elif attr == 'age': #返回方法
            return lambda:25
        else:
            raise AttributeError('\'Student\'has no attribute \'%s\'' % attr)
