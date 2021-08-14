from models import User
from db import db_session 
from sqlalchemy import Column, Integer, String, and_



def login(user_name):
    user_verification = correct_name(user_name)
    user_verification = User.query.filter(User.name == user_verification).first()
    if not user_verification:
        
        new_user = checking_new_user()
        new_password = checking_password()
        creat_new_user(new_user , new_password)
  
    else:
        verification_old_user(user_verification.id)



def correct_name(user_name):
    user_name_list = user_name.split()
    
    while len(user_name_list) == 0:
        user_name = input("Введите User name: ")
        user_name_list = user_name.split()

    return user_name.lower().strip()


def checking_new_user(): 
    user_existence = 1
    while user_existence:
        user = input("Такого пользователя не существует, для регистрации введите свой user_name: ")
        new_user = correct_name(user)
        user_existence = User.query.filter(User.name == new_user).first()

    return new_user
    
    
def creat_new_user(new_user , new_password):

    registration = User(
                name = new_user ,
                password = new_password
    )
    db_session.add(registration)
    db_session.commit()



    
def checking_password():
    print("Пароль должен состоять минимум из двух символов")
    new_password_1 = input("Введите пожалуйста свой password: ")
    new_password_2 = input("Повторите пожалуйста свой password: ")
    input_error(new_password_1 , new_password_2)

    while len(new_password_1) < 2 or (new_password_2 != new_password_1):
        new_password_1 = input("Введите пожалуйста свой password: ")    
        new_password_2 = input("Повторите пожалуйста свой password: ")
        input_error(new_password_1 , new_password_2)

    return new_password_2    


def input_error(new_password_1 , new_password_2):        
        if new_password_1 != new_password_2:
            print("Пароли не совпадают")
        elif len(new_password_1) < 2 or len(new_password_2) < 2: 
            print("!!!!Пароль должен состоять минимум из двух символов!!!!")
    

    


def verification_old_user(user_verification):
    if user_verification:
        password = input("Введите пожалуйста password: ")
        fit = password_fits(user_verification , password)       
        if fit:
            return print(f'Здравствуй пользователь { fit}')

def password_fits(user_verification , password):
    password_verification = User.query.filter(and_(User.id == user_verification , User.password == password)).first()
    while not password_verification:
        password = input("Введите пожалуйста password: ") 
        password_verification = User.query.filter(and_(User.id == user_verification , User.password == password)).first()
    return password_verification.name

if __name__ == '__main__':
    user_name = input("Введите пожалуйста свой user_name: ")
    login(user_name)