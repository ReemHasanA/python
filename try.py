class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
    
MyClass.i = 1000  # Modify the class variable
print(MyClass.i)  # Output: 1000
print(MyClass.f(MyClass))  # Output : hello world