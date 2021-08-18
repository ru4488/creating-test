from creating_test import creating_test
from add_and_edit import user_tests

# меню выбора

def main_menu(user_id):
    choice_in_main_menu = menu_features()
    if choice_in_main_menu == "1":
        print(5)
    elif choice_in_main_menu == "2":
        creating_test(user_id)
    elif choice_in_main_menu == "3":
        user_tests(user_id)



def menu_features():
    print("Пройти тест - 1 ")
    print("Создать тест - 2")
    print("Посмотреть свои тесты - 3")
    print("Редактировать тесты - 4")
    menu_feature = '1234'
    choice = input("Введите число:  ").strip()
    while choice not in menu_feature: 
        choice = input("Введите число:  ").strip()
    return choice

def add_or_edit():
    print("Для добавления вопросов в тест введите - 1 ")
    print("Для редактирования вопросов введите - 2")
    print("Для удаления вопросов введите - 3")
    print("Для просмотра существующих тестов нажмите - 4")
    choice = input("Введите число:  ").strip()
    menu_feature = '1234'
    while choice not in menu_feature: 
        choice = input("Введите число:  ").strip()
    return choice

def edit_or_delete():
    print("Для измененитя вопроса введите - 1")
    print("Для удаления вопроса введите - 2")
    choice = input("Введите число:  ").strip()
    menu_feature = '12'
    while choice not in menu_feature: 
        choice = input("Введите число:  ").strip()
    return choice

    



if __name__ == '__main__':
    user_id = 1
    main_menu(user_id)