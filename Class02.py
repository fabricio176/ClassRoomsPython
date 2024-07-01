# Output
print('Hello World')

'''

Comment's pad

'''

# Comment's line

# Variable
name = 'Fabas' #String
age = 22 #Integer
weight = 73 #integer
height = 1.73 #float
instructor = False #boolean - always init with uppercase

#Convert variable: use the method name and put the variable example str(age)
age = str(age)

# method type

print(type(height))

# Creating a Object in python
class Pessoa:
    def __init__(self, name, age, weight, height, instructor):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.instructor = instructor
        
pessoa1 = Pessoa('Fabas', 22, 73, 1.73, False)

print(pessoa1.name)
        

