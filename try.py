class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
    
MyClass.i = 1000  # Modify the class variable
print(MyClass.i)  # Output: 1000
print(MyClass.f(MyClass))  # Output : hello world
print(MyClass.__doc__)  # Output: A simple example class
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i  # Output: (3.0, -4.5)