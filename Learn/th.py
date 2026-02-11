from functools import wraps #you need this to perserve the original function when the wrapper is doing its job, this way you can chain decorators
def decorat(og):
    @wraps(og) #mandatory for chaining decorators
    def warp(*args, **kwargs): #need to put args and kwargs if functions will have many positional args
        print("Wrapper execute this")
        return og(*args, **kwargs)
    return warp
#we can also use decorators with classes 
class decorat_class():
    def __init__(self, og):
        self.og = og
    #good dunder, this method is used as the wrapper. Call method allows the instance of a class to be called as if it were a function
    def __call__(self, *args, **kwargs):
        print("call method executed this")
        return self.og(*args, **kwargs)

@decorat #this is the same as making an object passing this function as a function to be wrapped within the decorator
def og():
    print('hi')

#func = decorat(og)
#func()
#these 2 are the same as doing @decorat
@decorat_class 
def display_info(name:str, age:int):
    print(f"Name: {name}, Age {age}")

display_info('name', 'jerry')
# you can also chain decorators
@decorat_class
@decorat
def hi():
    print('hi')

hi()
#it is equivalent to doing func = decorat(decorat_class(hi)) -> func()
