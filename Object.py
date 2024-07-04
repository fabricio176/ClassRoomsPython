# Creating a Python class for a Person
class Person:
    def __init__(self, name, age, weight, height, instructor):
        """
        Initializes a Person object with name, age, weight, height, and instructor status.

        Args:
        - name (str): Name of the person.
        - age (int): Age of the person.
        - weight (float): Weight of the person.
        - height (float): Height of the person.
        - instructor (bool): True if the person is an instructor, False otherwise.
        """
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.instructor = instructor
        
# Function to create a new user and insert into a Person object
def insertUser():
    """
    Prompts the user to enter details and creates a new Person object based on the input.

    Returns:
    - Person: A Person object initialized with user-provided details.
    """
    name = input('Digite seu nome: ')
    age = int(input('Digite sua idade: '))
    weight = float(input('Digite seu peso (kg): '))
    height = float(input('Digite sua altura (m): '))
    instructor_input = input('Você é um instrutor?\nEnter sim or não: ')

    instructor = True if instructor_input.lower() == 'sim' else False

    user = Person(name, age, weight, height, instructor)
    return user

def addUser():
    """
    Allows the user to add multiple users and prints the total number of users added.
    """
    totalUsers = []

    while True:
        addNewUser = input('Você quer adicionar um novo usuário?\nDigite sim ou não: ')
        
        if addNewUser.lower() != 'sim':
            break
        
        user = insertUser() 
        totalUsers.append(user)
        print('Usuário adicionado com sucesso.')

    print('Total de usuários adicionados:', len(totalUsers))

addUser()
