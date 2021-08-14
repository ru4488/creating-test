from models import User , Test_name
from db import db_session 
from sqlalchemy import and_



def creating_test(user_id):
    name_of_test = input("Введите название теста: ")

    standardized_name = name_exists(name_of_test)
    
    new_test_name = check_new_test(standardized_name , user_id)

    creat_new_test(new_test_name , user_id)
    
      

def name_exists(name_of_test):
    test_name_list = name_of_test.split()

    while len(test_name_list) == 0:
        name_of_test = input("Введите название теста: ")
        test_name_list = name_of_test.split()

    return name_of_test.lower().strip()



def check_new_test(standardized_name, user_id):
    checking_the_name = Test_name.query.filter(and_(Test_name.name_of_test == standardized_name , Test_name.user_id == user_id)).first()  

    if checking_the_name:

        while checking_the_name:
            print("такое имя теста уже существует")
            name_of_test = input("Введите название теста: ")
            standardized_name = name_exists(name_of_test)
            checking_the_name = Test_name.query.filter(and_(Test_name.name_of_test == standardized_name , Test_name.user_id == user_id)).first()

    return standardized_name    


def creat_new_test(new_test_name , user_id):
    add_name = Test_name(
                user_id = user_id ,
                name_of_test = new_test_name )
   
    db_session.add(add_name)
    db_session.commit()
   

if __name__ == '__main__':
    user_id = 1
    creating_test(user_id)