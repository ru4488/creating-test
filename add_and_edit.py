from models import Test_name , Question
from db import db_session 
from sqlalchemy import and_


def add_question(user_id):
    choice = add_or_edit()

    if choice == "1":
        selected_test_id = choise_name_test(user_id)
        cicle_of_additions(selected_test_id)


def cicle_of_additions(selected_test_id):
    stop_word = "1" 
    while stop_word != "0":
        question_fit = correct_question(selected_test_id)
        creat_new_question(question_fit , selected_test_id)
        print("Для выхода введите '0'")
        print("Для добавления вопросов введите ¨1")
        print("Для просмотра существеющих вопросов введите ¨3")
        stop_word = input(":  ")
        if stop_word == "3":
            added_questions(selected_test_id , )
            



def added_questions(selected_test_id):
    all_question = Question.query.filter(Question.test_id == selected_test_id).all()
    selected_test = Test_name.query.filter(Test_name.id == selected_test_id).first()
    name = ''

    for row in all_question:      
        name += ( f' {row.question}; \n')


    print(f'В тест - {selected_test.id} добавлены вопросы:')
    print(name)






# проверка, присутствует ли такой вопрос в этом тесте или состоит он хотя бы из одного символа

def correct_question(selected_test_id):
    new_question = input('Введите вопрос: ').lower().strip()
    question_list = [] 
    question_list = new_question.split()
    presence = presence_question(new_question , selected_test_id)

    while len(question_list) == 0 or len(presence) == 0:                  
        if len(question_list) == 0:
            print("Вопрос должен состоять хотя бы из одного слова")
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
    # all_id = user_tests(user_id)
    user_choise_id = input("введите id теста: ").strip()
    while user_choise_id not in all_id:
        print("Теста с таким id у вас нет")
        user_choise_id = input("введите id теста: ").strip()

    all_test = Test_name.query.filter(and_(Test_name.id == user_choise_id , Test_name.user_id == user_id)).first()
    print(f"Имя теста {all_test.name_of_test}")
    return user_choise_id

# Все тесты вопросы 

def user_(user_id):
    all_question = Question.query.filter(Question.test_id == selected_test_id).all()
    name = ''

    for row in all_question:      
        name += ( f'id теста - {row.id}, навзвание теста - {row.name_of_test}; \n')


    print(f'В тест - {row.id} добавлены вопросы:')
    print(name)



# Все тесты пользователя, возвращает все id тестов пользователя 

def user_tests(user_id):
    all_test = Test_name.query.filter(Test_name.user_id == user_id).all()
    name = ''
    all_id = ''
    for row in all_test:      
        name += ( f'id теста - {row.id}, навзвание теста - {row.name_of_test}; \n')
        print(name)
        all_id += str(row.id)   
    print("Вам доступны тесты:")
    print(name)
    return all_id



if __name__ == '__main__':
    user_id = 1
    user_tests(user_id)
    add_question(user_id)