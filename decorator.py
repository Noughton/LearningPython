#装饰器
def now():
    print('2019')

print(now.__name__)

def log(func):
    def wrapper(*arge,**kw):
        print('call %s():' %func.__name__)
        return func(*arge,**kw)
    return wrapper

@log
def now_two():
    print('01')

now_two()