
#验证a += a和 a = a +a区别

def addNum(a):
    print(id(a))
    print('='*8)
    a += a
    print(id(a))
    
def addNum2(a):
    print(id(a))
    print('-'*8)
    a = a + a #开辟新的内存存放加后的数据，然后赋值给A
    print(id(a))
    
nums = [11,22]
print('nums id:')
print(id(nums))

addNum2(nums)
    
