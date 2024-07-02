# Creating a Object in python
class Pessoa:
    def __init__(self, name, age, weight, height, instructor):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.instructor = instructor
        
pessoa1 = Pessoa('Fabas', 22, 73, 1.73, False)


# Function to create a new User and insert into a Object
def insertUser():

    name = input('Digite o seu Nome :')
    age = int(input('Digite a sua Idade :'))
    weight = float(input('Digite o seu Peso :'))
    height = float(input('Digite a sua Altura :'))
    instructor = input('Você é um instrutor ?\n Digite sim ou não :')

    if(instructor == 'sim'):
        instructor = True
    else:
        instructor = False


    User = Pessoa(name, age, weight, height, instructor)

    return User


def addUser():

    addNewUser = True
    totalUsers = []

    if(addNewUser == True):
     newUser = input('Você deseja adicionar um novo usuário ?\n Digite sim ou não : ')     
     while newUser == 'sim':
            addNewUser = True
            User = insertUser() 

            totalUsers.append(User)

            print('Usuário Adicionado com sucesso')

            newUser = input('Você deseja adicionar um novo usuário ?\n Digite sim ou não : ')
            if(newUser == 'sim'):
                addNewUser = False   
    else:
        addNewUser = False   
  
    return print('Total de Usuários adicionados :', sum(totalUsers))

addUser()


        

