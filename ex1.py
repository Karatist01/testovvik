# # x = 5.4
# # s = "Hello"
# # print(type(x), type(s))
# msg = "сообщения"
# count = 0
# print(msg)
# numbers = [2, 1, 3, 4, 7]
# more_numbers = [*numbers, 11, 18]
# print(*more_numbers, sep=', ')
# fruits = ['lemon', 'pear', 'watermelon', 'tomato']
#
# print(fruits[0], fruits[1], fruits[2], fruits[3])
# # lemon pear watermelon tomato
# print(*fruits)
# # lemon pear watermelon tomato
# a*x = b
# x = b/a
# def linear_solve(a, b):
#     if a:
#         return b / a
#     elif not a and not b: # снова используем числа в логических выражениях
#         return "Бесконечное количество корней"
#     else:
#         return "Нет корней"

# a*x**2 + b*x + c = 0 - общий вид уравнения
# D = b**2 - 4*a*c - дискриминант
# Если D<0, то уравнение не имеет вещественных корней
# Если D=0, то уравнение имеет один корень - x = -b/(2*a)
# Если D>0, то уравнение имеет два корня
# x1 = (-b - D**0.5)/(2*a)
# x2 = (-b + D**0.5)/(2*a)
#
# P.S. D**0.5 - равносильно извлечению квадратного корня


# def discriminant(a, b, c):
#     D = b**2 - 4*a*c
#     return D
# a = 4
# b = 2
# c = None
# D = discriminant(a, b, c)
# D = Diskrimin
# print("Дискриминант D равен:", D)

# def D(a, b, c):
#     return b ** 2 - 4 * a * c

# def quadratic_solve(a, b, c):
#     if D(a, b, c) < 0:
#         return "НЕт вечественных корней"
#     elif D(a, b, c) == 0:
#
#        return -b / (2 * a)
#     else:
#         return (-b - D(a,b,c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)
#
#

# last = 0
# for a in e(): # e() - генератор
#     if (a - last) < 0.00000001: # ограничение на точность
#         print(a)
#         break # после достижения которого - завершаем цикл
#     else:
#         last = a # иначе - присваиваем новое значение
# import random
#
# def get_user_choice():
#     user_choice = input("Выберите камень (k), ножницы (n) или бумагу (b): ").lower()
#     while user_choice not in ['k', 'n', 'b']:
#         user_choice = input("Неверный ввод. Пожалуйста, выберите камень (k), ножницы (n) или бумагу (b): ").lower()
#     return user_choice
#
# def get_computer_choice():
#     return random.choice(['k', 'n', 'b'])
#
# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "Ничья!"
#     elif (user_choice == 'k' and computer_choice == 'n') or \
#          (user_choice == 'n' and computer_choice == 'b') or \
#          (user_choice == 'b' and computer_choice == 'k'):
#         return "Вы выиграли!"
#     else:
#         return "Компьютер выиграл!"
#
# def play_game():
#     print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
#     while True:
#         user_choice = get_user_choice()
#         computer_choice = get_computer_choice()
#         print(f"Ваш выбор: {user_choice}")
#         print(f"Выбор компьютера: {computer_choice}")
#         print(determine_winner(user_choice, computer_choice))
#         play_again = input("Хотите сыграть ещё раз? (да(1)/нет(2)): ").lower()
#         if play_again != '1':
#             break
#
# play_game()
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь неавторизован. Функция выполнена не будет")
#     return wrapper
#
# @is_auth
# def from_db():
#     print("some data from database")
#
# from_db()
# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# if auth:
#     username = input("Введите ваш username:")
#
# @is_auth
# @has_access
# def from_db():
#     print("some data from database")
#
# from_db()
#
# a = 4.33
# b = -4
# print(f"  КООРДИНАТЫ ТОЧКИ А РАВНЫ {a}, а кординаты точки б {b} равны ")
#

a = int(input())
b = abs(a)
print(b)