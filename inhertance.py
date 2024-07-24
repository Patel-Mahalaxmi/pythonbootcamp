'''class Animal:
    def Speak():
        return "Animal is speaking"
#single inheritance
class Dog(Animal):
    def Bark():
        return "bow.."
#multilevel inheritance
class Puppy(Dog,Animal):
    def puppy_speak():
        return "i am puppy"
    
#obj1=Animal
#obj2=Dog
obj3=Puppy
print(obj3.Speak())
print(obj3.Bark())
print(obj3.puppy_speak())

class Animal():
    def Speak():
        return "Speaking..."
class Dog(Animal):
    def Speak():
        return "Dog is speaking"
class Puppy():
    def Speak():
        return "puppy is speaking"
obj3=Puppy
print(obj3.Speak())'''
class Cal:
    def add(a,b,c):
        return a+b+c
obj1=Cal
print(obj1.add(1,2,3))
