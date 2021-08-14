from models import Test_name , Question
from db import db_session 
from sqlalchemy import and_




def add_and_edit(user_id):
    user_tests(user_id)
    choice = add_or_edit()

    if choice == "1":
        selected_test_id = choise_name_test(user_id)
        add_question(selected_test_id) 


def add_question(selected_test_id):
    new_question = input('Введите вопрос: ').lower().strip()
    question_fit = correct_question(new_question , selected_test_id)
    creat_new_question(question_fit , selected_test_id)
    



def correct_question(new_question , selected_test_id):
    question_list = [] 
    question_list = new_question.split()
    presence = presence_question(new_question , selected_test_id)

    while len(question_list) == 0 or len(presence) == 0:                  
        
        if len(question_list) == 0:
            print("Вопрос должен состоять хотбы из одного слова")
        else:
            print("Такой вопрос в тесте уже есть")

        new_question = input("Введите вопрос: ").lower().strip()
        question_list = new_question.split()
        presence = presence_question(new_question , selected_test_id)
        
       
    return new_question


def presence_question(new_question , selected_test_id):   
    presence = Question.query.filter(and_(Question.question == new_question , Question.test_id == selected_test_id)).first()
    if presence:
        return ''
    else: 
        return new_question


# добавляем вопрос в тест

def creat_new_question(question_fit , selected_test_id):
    add_question = Question(
                test_id = selected_test_id ,
                question = question_fit)
                
    db_session.add(add_question)
    db_session.commit()




# выбор нужного теста 

def choise_name_test(user_id):
    all_id = user_tests(user_id)
    user_choise_id = input("введите id теста: ").strip()
    while user_choise_id not in all_id:
        print("Теста с таким id у вас нет")
        user_choise_id = input("введите id теста: ").strip()

    all_test = Test_name.query.filter(and_(Test_name.id == user_choise_id , Test_name.user_id == user_id)).first()
    print(f"Имя теста {all_test.name_of_test}")
    return user_choise_id




# Все тесты пользователя, возвращает все id пользователя 

def user_tests(user_id):
    all_test = Test_name.query.filter(Test_name.user_id == user_id).all()
    name = ''
    all_id = ''
    for row in all_test:      
        name += ( f'id теста - {row.id}, навзвание теста - {row.name_of_test}; \n')
        all_id += str(row.id)   
    print("Вам доступны тесты:")
    print(name)
    return all_id

# меню выбора

def add_or_edit():
    print("Для добавления вопросов в тест введите - 1 ")
    print("Для редактирования вопросов введите - 2")
    print("Для удаления текста введите - 3")
    choice = input("Введите число:  ").strip()
    menu_feature = '123'
    while choice not in menu_feature: 
        choice = input("Введите число:  ").strip()
    return choice



if __name__ == '__main__':
    user_id = 1
    add_and_edit(user_id)