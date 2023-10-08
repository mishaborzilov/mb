# home_work = input('Сделал уроки?')
# if home_work == 'да':
#    print ('иди пеки пирожки')
# else:
#     print('Иди делай уроки')
# После if может стоять True или 1 и будет всегда совершаться 1 действие
# После if может стоять False или 0 и будет всегда совершаться 2 действие

# num = int(input())
# if num > 0:
# print('Число положительное')
# else:
# print('отрицательное')

# num = int(input())
# if num > 0:
# print('Число положительное')
# else:
# if num < 0:
# print('отрицательное')
# else:
# print('Число ноль')


# num = int(input())
# if num % 2 == 0 and num > 0:
# print('число четное')
# else:
# print('число нечетное')
# and либо и либо умножение
# or либо или либо плюс

# num = int(input())
# if num % 2 == 0 and num > 0:
# print('число четное')
# else:
# print('какое-то не такое')

# таблица истины
# x = 5 > 2 =true
# y = 7 % 2 =false

# x = (5 > 2) =true
# y = 7 % 2 =false

# либо = or

# year = int(input())
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
# print('год високосный')
# else:
# print('год не високсный')

# скобочки в 50 строке нужны чтобы сначало произошло действие в скобочках,
# а потом другое действие
# при решение мы получаем високосный год или нет(високосный год считатеся с нуля - 4
# тоесть 4-8 и тд, високосный год считается каждые 4 года с нуля)

# num1 = float(input())
# operand = input()
# num2 = float(input())
# if operand == '+':
# print(num1, operand, num2, '=', num1 + num2)
# if operand == '-':
# print(num1, operand, num2, '=', num1 - num2)
# if operand == '/':
# print(num1, operand, num2, '=', num1 / num2)
# if operand == '//':
# print(num1, operand, num2, '=', num1 // num2)
# if operand == '*':
# print(num1, operand, num2, '=', num1 * num2)
# if operand == '%':
# print(num1, operand, num2, '=', num1 % num2)

# num1 = float(input())
# operand1 = input()
# num2 = float(input())
# operand2 = input()
# num3= float(input())
# #+
# if operand1 == '+' and operand2 == '+':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 + num2 + num3)
# if operand1 == '+' and operand2 == '-':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 + num2 - num3)
# if operand1 == '+' and operand2 == '*':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 + num2 * num3)
# if operand1 == '+' and operand2 == '/':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 + num2 / num3)
# if operand1 == '+' and operand2 == '//':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 + num2 // num3)
# if operand1 == '+' and operand2 == '%':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 + num2 % num3)
# #-
# if operand1 == '-' and operand2 == '-':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 - num2 - num3)
# if operand1 == '-' and operand2 == '/':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 - num2 / num3)
# if operand1 == '-' and operand2 == '//':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 - num2 // num3)
# if operand1 == '-' and operand2 == '*':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 - num2 * num3)
# if operand1 == '-' and operand2 == '%':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 - num2 % num3)
#     #*
# if operand1 == '*' and operand2 == '*':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 * num2 * num3)
# if operand1 == '*' and operand2 == '//':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 * num2 // num3)
# if operand1 == '*' and operand2 == '/':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 * num2 / num3)
# if operand1 == '*' and operand2 == '%':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 * num2 % num3)
# #%
# if operand1 == '%' and operand2 == '%':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 % num2 % num3)
# if operand1 == '%' and operand2 == '//':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 % num2 // num3)
# if operand1 == '%' and operand2 == '/':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 % num2 / num3)
# #/
# if operand1 == '/' and operand2 == '/':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 / num2 / num3)
# if operand1 == '/' and operand2 == '//':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 / num2 // num3)
# #//
# if operand1 == '//' and operand2 == '//':
#     print(num1, operand1, num2, operand2, num3 ,'=', num1 // num2 // num3)
# калькулятор

# b=int(input())
# m=int(input())
# n=int(input())
# pol = 0
# nepol = 0
# if b > 0:
#     pol+=1
#     print('положительное')
# else:
#     nepol+=1
#     print('отрицательное')
# if m > 0:
#     pol+=1
#     print('положительное')
# else:
#     nepol+=1
#     print('отрицательное')
# if n > 0:
#     pol+=1
#     print('положительное')
# else:
#     nepol+=1
#     print('отрицательное')
# здесь мы пишем 3 числа и вычисляем какие положительные а какие не положительные

#  b=int(input())
#  m=int(input())
#  n=int(input())

#    if m > n and m > b:
#     print(m)
#    if m > n and m < b:
#     print(b)
#    if m < n and b < n:
#     print(n)

# b=int(input())
# m=int(input())
# n=int(input())

# if m > n and m > b:
#     print(m)
# if m > n and m < b:
#     print(b)
# if m < n and b < n:
#     print(n)
# if  b > n  and b < m :
#     print(b)
# if  n < m  and m < b :
#     print(n)
# a=int(input)
# b=int(input)
# m=int(input)
# if a>24:
#     print('часы до 24')
#     a=int(input)
# else:
#     print(a)
# if b>60:
#     print('минуты до 60')
#     b=int(input)
# else:
#    print(b)
# if m>60:
#    print('секунды до 60')
#    m=int(input)
# else:
#     print(b)


# month = int(input())
# if month == 12 or month == 1 or month== 2:
# print('зима')
# elif month == 3 or month == 4 or month== 5:
# print('весна')
# elif month == 6 or month == 7 or month== 8:
# print('лето')
# elif month == 9 or month == 10 or month== 11:
# print('осень')
# else:
# print('некоректный номер месяца')

# a = int(input())
# b = int(input())
# c = int(input())
# if not (0 <= a < 24):
#    print('неверное количество часов, число от 1 до 24.')
# elif not (0 <= b < 60):
#    print('неверное количество минут, число от 1 до 60.')
# elif not (0 <= c < 60):
#    print('неверное количество секунд, число от 1 до 60.')
# else:
#    print(a,':',b,':',c)

# a = int(input())
# b = int(input())
# c = int(input())
# if b == '-':
#    print(a-c)
# elif b == '+':
#    print(a+c)
# elif b == '/':
#    print(a/c)
# elif b == '*':
#    print(a*c)
# else:

# n1 = int(input())
# znak = input()
# n2 = int(input())

# username = input()
# if username.istitle():
#     print('корректное имя пользовтеля')
# else:
#     print('не корректное имя пользователя')

# num = int(input())
# #2,5
# a = num // 10
# b = num % 10
# if a>b:
#     print('старший больше')
# elif a<b:
#     print('младший больше')
# else :
#     print('разряды равны')

# a = int(input())
# b = int(input())
# c = int(input())
# if a > c + b and c < a + b and b < a + c :
#     print('правельный треугольник')
#     if a ==  b == c :
#        print('равносторонний')
#     elif a == b or a == c or c ==b:
#        print('равнобедренный')
#     else:
#        print('равнобедренный')
# else:
#     print('это не треугольник')
# score=0
# print('в ответах писать только цифру ответа')
# print('ВЫ ПОПАЛИ В ИГРУ"Кто хочет тот захочет"')
# answer1=('воооооопрос 1 Из какой страны родом Джастин Бибер? \n ВААААрианты ответов \n 1)Канада,\n2)США,\n3)Франция,\n4)Англия.\n Введите номер првильного ответа:')
# if answer1 == '1':
#     score += 100
#     print('верно Он также говорит на французском и английском языках, поскольку он родом из Онтарио, франко-канадской провинции, Ваш счет:', score )
#     print('играем дальше')
# answer2 = input('Можно ли квантовую механику и общую теорию относительности объединить в единую самосогласованную теорию (возможно, это квантовая теория поля)? \nВарианты ответов :\n1)нет,\n2)пока что нет,\n3)да,\n4)незаню')
# if  answer2 =='4':
#     score += 100
#     print('я сам незнаю так что Ваш счет:', score )
#     print('играем дальше')
# answer3 = input('Существуют ли в природе дополнительные измерения пространства-времени, кроме известных нам четырёх? \n1) так как по 5 закану вселенско теоретичекско механической теории это возможно при счете ,\n2)незнаю,\n3)нет,\n4)Это открытый вопрос. Пока физика не знает точного ответа на него. Число измерений может быть от известных четырёх до нескольких десятков.')
# if answer3 =='4':
#     score += 100
#     print('ПРАВИЛЬНО это открытый вопрос. Пока физика не знает точного ответа на него. Число измерений может быть от известных четырёх до нескольких десятков Ваш счет:', score )
#     print('играем дальше')
# answer4 = input('ААА теперь самый сложный вопрос 2+2 \nВАрианты ответов: \n1)2,\n2)незнаю,\n3)4,\n4)5.')
# if answer4 == '1':
#     score += 100
#     print('верно это будет 2 Ваш счет:', score )
#     print('Конец')

# try:
#    num = int(input())
#    print(num)
# except ValueError:
#       print('ошибка! вы ввели букву, а не число')
# print('программа работает дальше')
# # сдесь используя try except мы показываем ошибку пользователя, try  это как бы первое действие происходящие в коде,
# #  а excpept работает как else.

# try:
#    num = int(input())
#    print(num)
# except ValueError:
#       print('ошибка! вы ввели букву, а не число')
# else:
#     print('ошибок не возникло')
# finally:
#     print('ошибка обработана')
# print('программа работает дальше')

# finally является окончанием действия

# x1 = 25
# x2 = x1+15
# if x1 > x2:
#     print('x1 больше')
# elif x1<x1
#     print('другая ситуация')
# except Exception: 
#     print('проверь код')

# казак
# шалаш
# потоп

# word = input('введите слово')
# reversed_word = word[::-1]
# if word == reversed_word:
#    print('слова палиндром')
# else:
#    print('слова не палиндромы')
# try:
#    cnt = int(input())
#    n = cnt%10
#    if 5<=n<=9:
#     print(cnt,'хомячков')
#    elif 2<= n  <=4:
#     print(cnt,'хомячка')
#    elif n == 0:
#     print(cnt,'хомячков')
#    elif 11<=cnt%100<=19:
#     print(cnt,'хомячков')
# except ValueError:
#     print('неправельное количество хомячков')

# password = input()
# if len(password) < 6:
#     print('пароль слишком короткий')
#     # print( password.isupper())
#     # print( password.islower)
# elif not (not password.isupper() and not password.isupper()):
#     print('нужно использовать и маленькие и большие буквы')
# else:
#     print('все ОК')

# password = input()
# if len(password) < 6:
#     print('пароль слишком короткий')
#     # print( password.isupper())
#     # print( password.islower)
# elif not (not password.isupper() and not password.islower()):
#     print('нужно использовать и маленькие и большие буквы')
# elif not (not password.isdigit() and not password.isalpha()):
#     print('нужно использовать и буквы и цифры ')
# else:
#     print('все ОК')


# username=input()
# if username=='admin':
#     password=input()
#     if password =='123':
#         print('здраствуйте о мой господин')
#     else:
#         print('ну хз лол иди взламывай другой ак чел')
# else:
#         print('сам')
#         print('ну привет пупсик')


# n=input('день')
# b=input('месяц')

# if n+1
#    print(n+1)
# else:
#    print('введины не коректные данные'


# import random
# print(random.randint(0,10))
# import random нужен для писания рандомного числа от 0 до 10 ну или больше

# import turtle
# import time
# turtle.pensize(20)
# turtle.pencolor(('black'))
# #задаем начальную позицию
# turtle.penup()
# turtle.setpos(-300,200)
# turtle.pendown()
# turtle.forward(600)
# turtle.right(90)
# turtle.forward(400)
# turtle.right(90)
# turtle.forward(600)
# turtle.right(90)
# turtle.forward(400)
# turtle.penup()
# turtle.setpos(100,100)
# turtle.pendown()
# turtle.right(90)
# turtle.forward(100)
# time.sleep(15)
# from math import radians
# import turtle
# import time
# turtle.pensize(20)
# turtle.pencolor(('black'))
# turtle.penup()
# turtle.sety(-200)
# turtle.pendown()
# turtle.circle(200)
# time.sleep(5)

# from math import radians
# import turtle
# import time
# radius = int(input('R ='))
# size = int(input('size ='))
# turtle.pensize(size)
# turtle.penup()
# turtle.pencolor(('black'))
# turtle.sety(-radius)
# turtle.pendown()
# turtle.circle(radius)
# time.sleep(5)

# from random import randint
# num = randint(100000,999999)
# m = int(input('введите 6 любых чисел или вам конец'))
# if m ==num:
#     print('как ты угадал?')
# else:
#     print('ты не угадал gg братик')

# import time
# print('взлом програмы')
# time.sleep(1)
# print('1%')
# time.sleep(1)
# print('2%')
# time.sleep(1)
# print('3%')
# time.sleep(1)
# print('4%')
# time.sleep(1)
# print('5%')
# time.sleep(1)
# print('6%')
# time.sleep(1)
# print('7%')
# time.sleep(1)
# print('8%')
# time.sleep(1)
# print('9%')
# time.sleep(1)
# print('10%')
# time.sleep(1)
# print('11%')
# time.sleep(1)
# print('12%')
# time.sleep(1)
# print('13%')
# time.sleep(1)
# print('14%')
# time.sleep(1)
# print('15%')
# time.sleep(1)
# print('16%')
# time.sleep(1)
# print('17%')
# time.sleep(1)
# print('18%')
# time.sleep(1)
# print('19%')
# time.sleep(1)
# print('20%')
# time.sleep(1)
# print('50%')
# time.sleep(1)
# print('51%')
# time.sleep(1)
# print('52%')
# time.sleep(1)
# print('53%')
# time.sleep(1)
# print('54%')
# time.sleep(1)
# print('55%')
# time.sleep(1)
# print('58%')
# time.sleep(1)
# print('68%')
# time.sleep(1)
# print('69%')
# time.sleep(1)
# print('70%')
# time.sleep(1)
# print('71%')
# time.sleep(1)
# print('73%')
# time.sleep(1)
# print('74%')
# time.sleep(1)
# print('75%')
# time.sleep(1)
# print('76%')
# time.sleep(1)
# print('77%')
# time.sleep(1)
# print('78%')
# time.sleep(1)
# print('79%')
# time.sleep(1)
# print('80%')
# time.sleep(1)
# print('81%')
# time.sleep(1)
# print('82%')
# time.sleep(1)
# print('83%')
# time.sleep(1)
# print('84%')
# time.sleep(1)
# print('85%')
# time.sleep(1)
# print('86%')
# time.sleep(1)
# print('87%')
# time.sleep(1)
# print('88%')
# time.sleep(1)
# print('89%')
# time.sleep(1)
# print('90%')
# time.sleep(1)
# print('91%')
# time.sleep(1)
# print('92%')
# time.sleep(1)
# print('95%')
# time.sleep(1)
# print('97%')
# time.sleep(1)
# print('98%')
# time.sleep(1)
# print('99%')
# time.sleep(4)
# print('8376867674987678й879%')
# time.sleep(1)
# print('пока')

# from random import randint
# num = randint(1,3)
# print('Игра в наперстки')
# n = int(input('Под каким наперстком камень:'))
# if n == num:
#   print('Угадал')
# else:
#   print('не угадал')
# import time
# import turtle
# turtle.pensize(15)
# turtle.right(60)
# turtle.forward(200)
# turtle.right(120)
# turtle.forward(200)
# turtle.right(120)
# turtle.forward(200)
# time.sleep(3)

# import time
# import turtle
# a = int(input())
# turtle.pensize(15)
# turtle.right(60)
# turtle.forward(a)
# turtle.right(120)
# turtle.forward(a)
# turtle.right(120)
# turtle.forward(a)
# time.sleep(3)

# from random import randint
# import time
# num = randint(1,6)
# m = randint(1,6)
# print('игра начинается')
# print('заряжаем ривольвер')
# print('крутим барабан')
# print('выстрел через')
# print('1')
# time.sleep(1)
# print('2')
# time.sleep(1)
# print('3')
# time.sleep(2)
# if m == num:
#   print('FFFFFF')
# else:
#   print('повезло повезло')

# i = 0
# while i<10:
#     print(i)
#     i += 1
# если мы пишем десять то выведит числа от 0-10
# i = 0
# while i<10:
#     print(i)
# будет писаться бесконечное количество 0
# i = 0
# while i<10:
#     if i%2==0:
#        print(i)
#     i += 1
# будет записывать только числа делющийся на 2 без остатка
# a = int(input())# начало
# b = int(input())# конец
# i = a
# while i<b:
#     print(i)
#     i += 1
# вписывая два числа команда будет писать все возможные числа от а до б

# from random import randint
# a = int(input())# начало
# i = 0
# while i<=a:
#     print(randint(0,100))
# i +=1
# к числу которому ты ввел число + 1 будут показыватья все варианты от 1 - 100


# from random import randint
# a = int(input())# начало
# i = 0
# plus = 0
# minus = 0
# while i<a:
#   n = (randint(-100,100))
#   if n > 0:
#       plus +=1
#   else:
#       minus +=1
#       print(n)
#       i +=1
# print(plus,minus)
# программа считает сколько положительных и отрицательных чисел
# в рандомных количестве

# from random import randint
# a = int(input())# начало
# i = 0
# v = 0
# while i<a:
#     n = (randint(-100,100))
#     if n%5==0:
#         print(n)
#     i +=1
# будет записывать только числа делющийся на 5 без остатка


# import turtle
# turtle.speed(100)
# turtle.pensize(1)
# turtle.penup()
# turtle.setpos(0,-400)
# turtle.pendown()
# turtle.color('black')
# a = int(input()) # начало
# i = 0
# while i < a:
#   y = turtle.pos()[1]
#   turtle.sety(y+1)
#   turtle.circle(10 + i * 2)
#   i += 1
# turtle.done()

# import turtle
# turtle.speed(300)
# turtle.pensize(1)
# turtle.penup()
# turtle.setpos(0,-300)
# turtle.pendown()
# turtle.color('black')
# a = int(input()) # начало
# i = 0
# while i < a:
#   y = turtle.pos()[1]
#   turtle.sety(y-1)
#   turtle.circle(10 + i * 2)
#   i += 1
# turtle.done()

# import turtle
# turtle.speed(1000)
# turtle.pensize(5)
# turtle.color('black')
# i = 1
# while 1 < 50:
#    turtle.forward(10*i)
#    turtle.right(90)
#    turtle.forward(10*i)
#    turtle.right(90)
#    turtle.forward(15*i)
#    turtle.right(90)
#    turtle.forward(15*i)
# i += 1
# turtle.done()

# import turtle
# turtle.speed(1000)
# turtle.pensize(1)
# turtle.color('black')
# i=1
# while i<250:
#     turtle.circle(300)
#     turtle.right(2)
#     turtle.forward(1)
#     i+=1
# turtle.done()

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


# a = int(input('число a:'))
# b = int(input('число b:'))
# while a<=b:
#     if a % 3 == 0:
#         print(a)
#         a+=1

# import turtle
# turtle.shape("turtle")
# turtle.fd(100)
# turtle.exitonclick()
# import turtle

# 1 turtle.title("Turtle Circles")
# circ = turtle.Turtle()
# circ.pencolor("purple")
# circ.fillcolor("orange")
# circ.shape("circle")
# circ.pensize(5)
# circ.speed(10)
# circ.fd(150)
# circ.begin_fill()
# circ.circle(90)
# circ.end_fill()

# n = 10
# t = turtle.Turtle()
# while n <= 50:
#     t.circle(n)
#     n += 10
# turtle.exitonclick()

# import turtle

# 2# Основные цвета для персонажа
# BODY_COLOR = 'red'
# GLASS_COLOR = 'skyblue'

# # Главный объект
# t = turtle.Turtle()


# # Метод для рисования тела
# def body():
# 	t.pensize(30) # Размер кисти

# 	t.fillcolor(BODY_COLOR) # Цвет заполнения
# 	t.begin_fill()

# 	# Сторона справа
# 	t.right(90)
# 	t.forward(50)
# 	t.right(180)
# 	t.circle(40, -180)
# 	t.right(180)
# 	t.forward(200)

# 	# Голова
# 	t.right(180)
# 	t.circle(100, -180)

# 	# Сторона слева
# 	t.backward(20)
# 	t.left(15)
# 	t.circle(500, -20)
# 	t.backward(20)

# 	t.circle(40, -180)
# 	t.left(7)
# 	t.backward(50)

# 	t.up()
# 	t.left(90)
# 	t.forward(10)
# 	t.right(90)
# 	t.down()

# 	t.right(240)
# 	t.circle(50, -70)

# 	t.end_fill()


# # Рисуем очки
# def glass():
# 	# Передвигаем черепашку
# 	t.up()
# 	t.right(230)
# 	t.forward(100)
# 	t.left(90)
# 	t.forward(20)
# 	t.right(90)
# 	t.down()

# 	# Устанавливаем цвет
# 	t.fillcolor(GLASS_COLOR)
# 	t.begin_fill()

# 	t.right(150)
# 	t.circle(90, -55)

# 	t.right(180)
# 	t.forward(1)
# 	t.right(180)
# 	t.circle(10, -65)
# 	t.right(180)
# 	t.forward(110)
# 	t.right(180)

# 	t.circle(50, -190)
# 	t.right(170)
# 	t.forward(80)

# 	t.right(180)
# 	t.circle(45, -30)

# 	t.end_fill()


# # Рисуем рюкзак
# def backpack():
# 	t.up()
# 	t.right(60)
# 	t.forward(100)
# 	t.right(90)
# 	t.forward(75)

# 	t.fillcolor(GLASS_COLOR)
# 	t.begin_fill()

# 	t.down()
# 	t.forward(30)
# 	t.right(255)

# 	t.circle(300, -30)
# 	t.right(260)
# 	t.forward(30)
# 	t.end_fill()


# # Вызываем все необходимые методы
# body()
# glass()
# backpack()

# turtle.done()


# 3import turtle

# turtlePen = turtle.Turtle()
# window = turtle.Screen()

# window.bgcolor("black")


# def polygon(n, size=80):
#     if n > 2:
#         angle = 360 / n

#         for n in range(0, n):
#             turtlePen.left(angle)
#             turtlePen.forward(size)


# turtlePen.speed(100)

# colors = ['orange', 'cyan', 'blue', 'green', 'red']

# size = 40
# for i in range(0, 60):
#     turtlePen.color(colors[i % 5])
#     polygon(4, size)
#     turtlePen.left(5)
#     size = size + 3

# window.mainloop()


# summa = 0
# price = input()
# while price !='end':
#     summa += int(price)
#     price = input()
# print(summa)

# summa = 0
# count = int(input('количество'))
# i = 1
# while i <= count:
#     print('#'*i)
#     i+=1


# a = int(input('введите первую оценку:'))
# b = int(input('введите вторую оценку:'))
# c = int(input('введите третью оценку:'))
# v = int(input('введите четвертую оценку:'))
# i = 0
# print(a+b+c+v)/4
# f=(a+b+c+v)/4
# if f>4.6:
#     print('ура побееда')
# else:
#     print(':(')


# summa = 0
# i = 0
# while i <4:
#     mark = int (input())
#     summa += mark
#     i+=1
# print(summa/4)
# if (summa/4) < 4:
#      print('грустно :((')
# else:
#      print('ура побееда')

# i = 10
# while i<=40:
#     if i%2==0:
#         print(i, 'котиков')
#     i+=1

# summa = 0
# i = 1
# while i<100:
#     summa += i
#     i+=1
# print(summa)


# a = int(input())
# a = int(input())
# summa = 0
# i = 1
# while i<100:
#     summa += i
#     i+=1
# print(summa)


# i=0
# solnce = True
# while solnce:
#     print('beg')
#     print('beg')
#     print('beg')
#     i+=1
# else:
#     print('shower')
# print('Next code')
# код при котором спорстмен будет бегать пока не сядит солнце

# i=0
# solnce = True
# while solnce:
#     i +=1
#     print(i,'beg befor continue')
#     if i%2==0:
#         continue
#     print(i,'beg after continue')
#     print(i,'beg')
#     i+=1
#     if i > 10:
#         solnce = False
# else:
#     print('shower')
# print('Next code')


# i=0
# solnce = True
# while solnce:
#     i +=1
#     print(i,'beg befor continue')
#     if i%2==0:
#         continue
#     print(i,'beg after continue')
#     if i==9:
#         print(i,'break')
#         break
#     print(i,'beg after break')
#     if i > 10:
#         solnce = False
# else:
#     print('shower')
#     print('end into loop whike')
# print('Next code')

# for verable in 1,2,3,4,5:
#     print(verable)
# for verable in '1,2,3,4,5':
#     print(verable)

# for verable in range(5):
#     print(verable)

# for verable in range(1,5):
#     print(verable)

# for verable in range(1,5,2):
#     print(verable)

# for verable in range(-10,-20,-2):
#     print(verable)


# a=[1,2,3,4,5]
# for i in a:
#     if 1%2==0:
#        print(i)
# for i in range(len(a)):
#     if a[i]%2==0:
#         print(a[i])


# sum_ = 0
# for i in range(1,100):
#    sum_ +=1
# print(sum_)

# a,b = int(input('введите число:')), int(input('введите число:'))
# for i in range(a,b + 1):
#     print(i)
# while a<b +1:
#     print(a)
#     a+=1

# b = int(input('ярусов:'))
# for i in range(1,b+1):
#     print('#'*i)

# b = int(input('ярусов:'))
# for i in range(1,b+1):
#     print('#'*i)
# for i in range (b):
#    for j in range(i):
#        print('#', end='')
# print()


# b = int(input('ярусов:'))
# s = input('символ:')
# for i in range(1,b + 1):
#    print(' '*(b-i)+s*i*2)
#    print('')


# b = int(input('ярусов:'))
# s = input('символ:')
# print(' '*(b-1)+chr(127775))
# for i in range(1,b + 1):
#    print(' '*(b-i)+s*i*2)
# print(' '*(b-1) + '||')

# a,b = 5,5
# print(str(a)+'+'+str(b)+'='+str(a+b))
# print(a,'+',b,'+',a+b)
# print('{} + {} = {}'. format(a,b,a+b))
# print(f'{a} + {b} = {a + b}')
# print('%d + %d = %d'%(a,b,a+b))


# print('введите число:')
# s = input('умножаемое число')
# for i in range(1,11):
#     print(f'{s} x {i} = {s*i}')

# a =int(input('ширина:'))
# b =int(input('высота:'))
# for i in range(b):
#     for i in range(a):
#         print('#',end='')
# print()
# print('________')
# for i in range(b):
#     print('#'*a)

# итерация, срез


# a = 0
# m = 10
# for i in range(7):
#     a+=m
#     m*=1.1
# else:
#     print(a)

# user = {
#     'name' : 'андрей',
#     'last name' : 'tunikov',
#     'age' : 17
#        }
# print(user['name'])

# text = ' - hallo world? -hallo brooo! - how today? -  i am god'
# word =  list(set(text.split()))
# print(word)

# word_count  = {}
# text = ' - hallo world? -hallo brooo! - how today? -  i am god'
# word =  text.split()
# for wrd in word:
#     if wrd in word_count:
#       word_count[wrd] = word_count(wrd)+1
#     else:
#         word_count[wrd] = 1
# print(word_count)

# price = {
#         'milk':69,
#         'chiken ':108,
#         'chokolate':999,
#         'streps':56
# }
# check = {}
# while True:
#     buy = input()
#     if buy.lower()=='end':
#        print('расчет окончен с вас:')
#        break
#     key,count = buy.split()
#     check[key] = int(count)
# summa = 0
# for key, count in check.items():
#    summa +=price [key] * count
# print(summa,' рублей')

# from random import randint


# cubs_sum = ()
# for key in range(2,13):
#     values = []
#     for i in range(1,7):
#         for j in range(1,7):
#            if i + j == key:
#             values.append((i,))
#     cubs_sum[key] = values
# a = randint(1,6)
# b = randint(1,6)
# print(cubs_sum[a+b])
# for key, values in cubs_sum.items():
#     print(key,values,sep=':')

# word_count = {}
# text = 'привет пока привет пока привет пока привет пока привет пока привет пока привет'
# word = text.split()
# for wrd in word:
#    if wrd in word_count:
#       word_count[wrd] = word_count[wrd] + 1
#    else:
#        word_count[wrd] = 1
# print(word_count)
# values = list(word_count.values())
# keys = list(word_count.keys())
# max_values = max(values)
# ind_max_value = values.index(max_values)
# print(keys[ind_max_value])

# user = {
#     'name' : 'андрей',
#     'last name' : 'tunikov',
#     'age' : 17,
#     'port':3,
#     'rarka':48
# print(user['name'])


# def is_sorted(arr):
#     if arr==sorted(arr):

#         return True
#     else:
#         return False

# nums=[1,2,3]
# is_sorted(nums)

# nums2=[6778, 478,247,654676]
# is_sorted(nums2)


# def find_longest(arr):
#     print(arr)
#     lens=[len(word)for  word in wordS]
#     max_lens=max(lens)
#     ind=lens.index(max_lens)
#     return arr[ind]

#     wordS=["огурец","тебе","дам"]

#     find_longest(wor
# def zip_longest_sum (arr):
#     print
#     spisok1=(1,2,3,5,3,53)
#     spisok2=(55,6,4,54,44,44,64)

# def join(x,y):
#     list = []
#     index = 0
#     if y == []:
#      return y [0]
#     else:
#         for i in range(len(y)):
#     f = y(index) + x
#     list.append(c)
#     index +=1

# def func(a ,b ):
#     return a + b
# print(func(5,6))


# def func(a = 1,b = 1):
#     return a + b
# print(func(5))

# def funs(*arr):
#     print(arr)
#     return sum(arr)
# print(func(2,3,4,4,5,64,646,46,46,6,46,4,6,46,6,46))


# def funs(a,b,c):
#     return a,b,c
# print(funs(b=3,c=2,a=4))

# лямбда функция
# lambda_funs =lamba a,b:
# print(a,b)

# simple_funs =lamba a,b: a + b
# print(funs)


# words =('я','ты','арбуз','об','голову')
# words.sort()
# print(words)

# words =('я','ты','арбуз','об','голову')
# words.sort(key=lambda w:len(w), reverse = True)
# print(words)


# fron random import randint
# def i():
#    return randint(1,6 )
# def round(b):
#    result = []
#    for i in range (1,b + 1):
#    c = i()
#    print(f,'block №{i} - {c}')
#    result.append(c)
#    print(f'сумма:{sum(result)}')
# def main():
#   cubes = int(input('скок кубов используется бро\n:'))
#    while = True:
#      round(cubes)
#     next = input('продолжить?(y,n)\n:')
#     if next.lower() !='y'
#        print(' выход из игры..')
#        sleep(0.5)
#        break
# main()


# from random imporn randint
# from pprint imporn randint
# def chek_let(let):
#     if let.isdigit() or let.sialpha():
#        return True
#     return False
# def get_short_url(url):
#    key = ''
#    while len(key) !=6:
#    for i in range(6):
#      let = url[randint(0,len(url) - 1)]
#      if print(chek_let(let))
#          key+=let
#     data_url[key] = url
# data_url = {}
# get_short_url('jdurhvhlgjijkhkadhfg')
# print(data_url)


# def fa(a,b):
#     x=a*b
#     return x
# fa(2,1)
# def fb(a,b):
#     x=a/b
#     return x
# fb(8,2)
# def fc(a,b):
#     x=a+b
#     return x
# fc(5,7)
# def fh(a,b):
#     x=a-b
#     return x
# fh(3,2)
# def fo(a,b):
#     x=a/b
#     return x
# fo(6,2)
# def fp(a,b):
#     x=a-b
#     return x
# fp(8,8)


# def print_area(area):
#     print('игровое поле')
#     print('------')
#     print(f'|{area[0]}|{area[1]}|{area[2]}')
#     print('------')
#     print(f'|{area[3]}|{area[4]}|{area[5]}')
#     print('------')
#     print(f'|{area[6]}|{area[7]}|{area[8]}')
#     print('------')

# def round(player,area):
#     combo = [
#         [0,1,2],
#         [3,4,5],
#         [6,7,8],
#         [0,3,6],
#         [1,4,7],
#         [2,5,8],
#         [0,4,8],
#         [6,4,2]
#     ]
#     p = {1:'певый',-1:'второй'}
#     values = {1:'x',-1:'0'}
#     while True:
#      num = int(input(f'ходит{p[player]} игрок\n номер клетки:'))
#      if area [num - 1] == ' ':
#         area[num - 1] = values[player]
#         break
#      else:
#         print('эта клетка уже занята')
#     print_area(area)
# for combo in combo_variant:
#     if area[combo[0]] == 'x' and area [combo[1]] == 'x' and area[combo[2]] == 'x':
#         return 'победил первый игрока'
#     if area[combo[0]] == '0' and area [combo[1]] == '0' and area[combo[2]] == '0':
#         return 'победил первый игрока'
# def main():
#     area = [' ' for i in range(9)]
#     player = 1
#     while True:
#         round(player, area)
#         player*=-1
# main()


# # x1 - курица, x2 - коровы
# def animals(x'головы', y'ноги'):
#   x1*x- y2
#   x2 y2 - x
#   if y2==0 and x1= 0and x2=0:
#         return x1,x2
#   else:
#         return 'нет решения'                                                                                                          задача 2)Четным или нечетным:                                                                                         def Even_or_Odd(num):


#   if num % 2 == 0:
#     return "Even"
#   else:
#     return "Odd"


# import random
# men = ['''

#       +---+
#       |   |
#           |
#           |
#           |
#           |
#   =========''','''

#      +---+
#      |   |
#      O   |
#          |
#          |
#          |
#   =========''','''

#      +---+
#      |   |
#      O   |
#      |   |
#          |
#          |
#   =========''','''

#      +---+
#      |   |
#      O   |
#     /|   |
#          |
#          |
#   =========''','''

#      +---+
#      |   |
#      O   |
#     /|\  |
#          |
#          |
#   =========''','''

#      +---+
#      |   |
#      O   |
#     /|\  |
#     /    |
#          |
#   =========''','''

#      +---+
#      |   |
#      O   |
#     /|\  |
#     / \  |
#          |
#   =========''']
# a = ['яблоко','банан','свекла','огурец','киви','гречка','ананас', 'банан', 'чай', 'мид', 'урок', 'максим', 'кавказкий фрукт']
# b = random.choice(a)
# print(b)
# print("тема еда и другие слова")
# chances = 0
# lat = [" _ "] * len(b)
# for leter in lat:
#     print(leter, end=' ')
# print()

# while  lat != list(b) and chances < len(a) - 1:
#     g = input("Введите букву: ")

#     if g in b:
#         print("правильно!")
#         for index, later in enumerate(b):
#             if later == g:
#                 lat[index] = later
#         print(lat)
#     else:
#         if chances == len(b):
#             break
#         chances = chances + 1
#         print("буква не угадана")
#         print('\n осталось:', chances, 'попыток')
#         print(men[chances])
# if chances < len(b):
#     print('ты выиграл')
# else:
#     print('game over')
# # import random
# # a = ['ананас', 'банан', 'чай', 'мид', 'урок', 'максим', 'кавказкий фрукт']
# # b = random.choice(a)
# # def print_area(area):
# #     print('тема любая')
# # while True:
# #     letter = input('ваша буква:')

# #     if letter in b:
# #         pass
# #     else:
# #         pass
# # b = []

# import easygui
# title = 'первая програма'
# easygui.msgbox('hallo world','первая программа','кнопка ок',image = '123.png')
# result = easygui.enterbox('этот блок как input',title,default='')
# if result:
#    print(result)
# btn_labol = easygui.buttonbox('этот блок с набором кнопок',title,['кнопка 1','кнопка 2','кнопка 3'])
# print(btn_labol)
# num = easygui.integerbox('в этом блоке можно вводить числа',title,lowerbound=10,upperbound=20)
# print(num)
# status = easygui.boolbox('это блок котрый с 2 вариантами ответов и вернет да или нет тоесть True или false',title,['ды','ноу'])
# print(status)
# import random


# import easygui
# import random
# words = ['редиска', 'тыква']
# def show_word(word, letters):
#     # word -> загаданное слово
#     # letters -> список правильно угаданных букв
#     result = ['_' for i in range(len(word))]
#     for i in range(len(word)):
#         if word[i] in letters:
#             result[i] = word[i]
#     return result

# def main():
#     secret_word = random.choice(words)
#     true_letters = []
#     all_letters = []
#     life = 8
#     while True:
#         letter = easygui.enterbox('Введите букву: ', title)
#         if len(letter) != 1:
#             if not easygui.msgbox('Можно вводить только одну букву!',title):
#                break
#             continue
#         if letter in all_letters:
#             if not easygui.msgbox('Такая буква уже есть.',title):
#                break
#             continue
#         all_letters.append(letter)
#         if letter not in secret_word:
#             life -= 1
#             if not easygui.msgbox(f'Неправильно. У вас осталось {life} жизней.',title):
#                 break
#             if life == 0:
#                 easygui.msgbox('Вы проиграли.',title)
#                 break
#         else:
#             true_letters.append(letter)
#             result = show_word(secret_word, true_letters)
#             if not easygui.msgbox(result):
#                 break
#             if '_' not in result:
#                 easygui.msgbox('Вы победили!')
#                 break

# main()


# alpha_str='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# alpha_list=list(alpha_str)
# alpha_list_reversed=alpha_list[::-1]
# text = 'хахахахаахахх я псих бегите ахахахахах'
# result = ''
# for let in text:
#     if let.lower() in alpha_list:
#       let_ind=alpha_list.index(let.lower())
#       new_let=alpha_list_reversed[let_ind]
#       result+=new_let
#     else:
#         result+=let
# print(result)


# import easygui
# def art_el(text):
#    result = ''
#    for let in text:
#       if let.lower() in alpha_list:
#         let_ind=alpha_list.index(let.lower())
#         new_let=alpha_list_reversed[let_ind]
#         result+=new_let
#       else:
#         result+=let
#    return result

# def art_1(text):
#    result = ''
#    for let in text:
#       if let.lower() in alpha_list:
#         let_ind=alpha_list.index(let.lower())
#         new_let=alpha_list_reversed[let_ind]
#         result+=new_let
#       else:
#         result+=let
#    return result

# alpha_str='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# alpha_list=list(alpha_str)
# alpha_list_reversed=alpha_list[::-1]
# text = 'хахахахаахахх я псих бегите ахахахахах'

# a = art_el(text)
# print(a)
# print(art_1(a))


# from easygui import *
# def art_el(text):
#    result = ''
#    for let in text:
#       if let.lower() in alpha_list:
#         let_ind=alpha_list.index(let.lower())
#         new_let=alpha_list_reversed[let_ind]
#         result+=new_let
#       else:
#         result+=let
#    return result

# def art_1(text):
#    result = ''
#    for let in text:
#       if let.lower() in alpha_list:
#         let_ind=alpha_list.index(let.lower())
#         new_let=alpha_list_reversed[let_ind]
#         result+=new_let
#       else:
#         result+=let
#    return result
# def art_el2(text,key = 3):
#    key = int(key)
#    for let in text :
#     if let in alpha_list:
#        let_ind = alpha_list.index(let.lower())
#        new_ind = let_ind + key
#        new_let = alpha_list[new_ind % 33]
#        result += new_let
#     else:
#         result += let
#    return result
# alpha_str='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# alpha_list=list(alpha_str)
# alpha_list_reversed=alpha_list[::-1]
# text = 'хахахахаахахх я псих бегите ахахахахах'

# main_title = 'ibahjdrf'
# def main():
#     msgbox('команда для щифрования от МЕНЯ АХХАХАХАХХАХАХАХАХ ой ой ладно иди дальше',main_title)
#     alg=buttonbox('fhafb вЫЫЫЫбери ахах алгоритм Шифровки',main_title, choices=['Шифр ООООТ меня ахахах','щифр фхфхфхфх и от меня тоже хахах'])
#     if alg =='Шифр ООООТ меня ахахах':
#        text = enterbox('ведДИ тЕЕЕкст хахаххаахаххаха\n\nввведи текст ааххаха:')
#        cod_result = art_el(text)
#        msgbox(f'результат шифрования:\n\n >>{cod_result}')
#     elif alg =='щифр фхфхфхфх и от меня тоже хахах':
#          text = multenterbox('шифрования моим способом \n\nввведи тектс и ключ ааххаха',main_title,['ключ','сообщеие'])
#          oper = buttonbox('выберите аахха опрецию обработки',main_title,['расшифровать илин ет','зашифрааахахахвотя'])
#          if oper == 'зашифрааахахахвотя':
#            cod_result = art_el2(text, key=3)
#          elif oper == 'расшифровать илин нет':
#            cod_result = art_el2(text, -int(key=3))
#          msgbox(f'результат шифрования:\n\n >>{cod_result}')
#     else:
#         return
# main()


# работа с файлами идет в 3 этапа
# открыть
# обработать
# закрыть
# режим открытия файла
# 'r' <---- читать
# 'w' <---- записать файл, стерев все старые данные в нем
# 'a' <---- записать файл, сохранив все старые данные в нем

# file = open('data.txt','r')
# print(file.read())
# file.close()
# возращает строку


# file = open('data.txt','r')
# print(file.readlines())
# file.close()
# #выводит список


# примеры для режима открытия файла 'a'
# from time import sleep
# for i in range(100):
#   file = open('data.txt','a')
#   file.write(str(i)+'\n')
#   file.close()
#   sleep(0,5)

# конструкция для работы с файлами, где файл закрывается автомотически после выполнения действий с данными
# with open('data.txt','r') as file:
#     data = file.read(10)
# print(data)
# for line in file:
#    print(line)

# a=0
# print('ввод: ')
# while True:
#    a+=1
#    text =  input(a)
#    if not text:
#       print('файл сохранен.')
#       break
#    file = open('data.txt','a')
#    file.write(f'{a}){text} '+ '\n')
#    file.close()


# file_m = input('введите название файла: \n>>')
# print('Ввод данных: ')
# i = 1
# while True:
#   text = input('>> ')
#   if not text:
#     print('файл сохранен')
#     break
#   file = open(file_m,'a')
#   file.write(f'{i}) {text}\n')
#   file.close()
#   a+=1


# i = 0
# file_m = str(input('введите название файла:>>'))
# file = open(file_m,'r')
# for line in file:
#    print(f'{line}', end='')
# file.close()


# i = 0
# file_m = str(input('введите название файла:>>'))
# i+=1
# text =  input(i)
# if not text:
#  print('')
# file = open(file_m,'r')
# for line in file:
#     print(f'{line}', end='')
# file.close()


# f = open('data.txt','r')
# line = f.readlines()
# n=int(input())
# print(line[:n])


# f = open('data.txt','r')
# line = f.readlines()
# n=int(input())
# print(line[-n:])


# try:
#     file_name = input()
#     file = open(file_name,'r',encoding='UTF-8')
#     data = file.readlines()
#     file.close()
# except FileNotFoundError:
#     print('такого фала нет дружочек пирожочек :(')
# else:
#     print(data)
# finally:
#     print('программа завершина:)')


# try:
#     file_name = input()
#     file = open(file_name,'r',encoding='UTF-8')
#     data = file.readlines()
#     sum = 0
#     for num in data:
#         sum += int(num)
#     file.close()
# except FileNotFoundError:
#     print('такого фала нет дружочек пирожочек :(')
# else:
#     print(data)
#     print('сумма всех чисел в файле =',sum)
# finally:
#     print('программа завершина:)')


# try:
#     file_name = input()
#     file = open(file_name,'r',encoding='UTF-8')
#     data = file.readlines()
#     sum = 0
#     for num in data:
#         sum += int(num)
#     file.close()
# except FileNotFoundError:
#     print('такого фала нет дружочек пирожочек :(')
# except ValueError:
#     print('прости но в файле должны содержаться только числа:(')
# else:
#     print(data)
#     print('сумма всех чисел в файле =',sum)
# finally:
#     print('программа завершина:)')


# from easygui import*
# try:
#     msgbox('выберите файл который хотите прочитать')
#     file_name = fileopenbox('выберите файл', filetypes=['*.txt'], default='*.txt')
#     file = open(file_name,'r',encoding='UTF-8')
#     data = file.readlines()
#     sum = 0
#     for num in data:
#         sum += int(num)
#     file.close()
# except FileNotFoundError:
#     msgbox('такого фала нет дружочек пирожочек :(')
# except ValueError:
#     msgbox('прости но в файле должны содержаться только числа:(')
# else:
#     msgbox(f'сумма всех чисел в файле ={sum}')
# finally:
#     msgbox('программа завершина:)')


# from easygui import*
# try:
#     text = enterbox('введите текст:')
#     msgbox('выберите файл который хотите сохранить')
#     file_name = filesavebox('выберите файл', filetypes=['*.txt'], default='file.txt')
#     file = open(file_name,'a',encoding='UTF-8')
#     file.write(text +'\n')
#     file.close()
# except FileNotFoundError:
#     msgbox('такого фала нет дружочек пирожочек :(')
# except Exception:
#     msgbox('произошла непревиденная ошибка')
# else:
#     msgbox('запись прошла хорошо пупсик')
# finally:
#     msgbox('программа завершина:)')

# try:
#     file_name  = 'nums.txt'
#     file = open(file_name,'r',encoding='utf-8')
#     nums = file.readlines()
#     c_nums = len(nums)
#     sum_nums = 0
#     for num in nums:
#        sum_nums +=int(nums)
#     av = sum_nums / c_nums
#     file.close()
# except FileNotFoundError:
#     print('файл не найден')
# except ZeroDivisionError:
#     print('файл пустой')
# except ValueError:
#     print('в файле могут быть только числа')
# except Exception:
#     print('возникла непредвиденная ошибка')
# else:
#    print(f'среднее значение: {av}')
# print(av)


# file_name = 'olimp.txt'
# file = open(file_name,'r',encoding='utf-8')
# data = file.readlines()
# max_score = 0
# for st in data:
#     st_list = st.split()
#     st_score = int(st_list[-1])
#     if max_score > st_score:
#         max_score = st_score
# file.close()
# print(max_score)


# try:
#    file = open('olimp.txt')
#    ld = 0
#    wm = 0
#    sv = 0
#    for ln in file:
#     ld += 1
#     wm += len(ln.split())
#     sv += len(ln.strip('\n'))
#     print('строк:', ld)
#     print('слов:', wm)
#     print('символов:', sv)
#     sum = ld + wm + sv
#     print('всего:',sum)
#     file.close()
# except FileNotFoundError:
#    print('файл не найден')
# except Exception:
#    print('возникла непредвиденная ошибка')


# try:
#    file = open('olimp.txt', 'r',encoding='utf-8')
#    a = input()
#    for i in file:
#       a += len(i.strip('\n'))
#       file.close()
#       print('таких числе всего:',a)
# except FileNotFoundError:
#    print('файл не найден')
# except Exception:
#    print('возникла непредвиденная ошибка')


# import json
# user = {
#     "us.name":"banixop",
#     "lvl": 99,
#     "email":"banixop@gmail.com",
#     "items":[
#     "knife",
#     "m4a1",
#     "DigLOOs"
#     ]
# }
##запись в файл
# file = open("data.json","w")
# json.dump(user,file)

##чтение файла
# file = open("data.json","r")
# data = json.load(file)
# print(data)
# file.close()


# data = {}
# import json
# print('вводите данные в формате:"ключ: значение"')
# while True:
#    item = input('>> ')
#    if not item:
#       break
#    key, value = item.split(':')
#    data[key] = value
# file = open('data.json','w',encoding='UTF-8')
# json.dump(data,file,ensure_ascii=True)
# file.close()


# import json
# file = open("data.json",'r')
# data = json.load(file)
# file.close()
# print(data)
# for i in range(len(data)):
#    item = data[i]
#    if type(item) is str:
#     data[i] += '!'
#    if type(item) is bool:
#     data[i] = not data[i]
#    if type(item) is int or type(item) is float:
#     data[i] += 1
#    if type(item) is list:
#     data[i] *= 2
#    if type(item) is dict:
#     data[i] ["newkey"] = None
# while None in data:
#     data.remove(None)
# file = open('data.json','w')
# json.dump(data,file)
# file.close()


# import json
# file = open("data.json", 'r')
# data = json.load(file)
# print(data)
# file.close()
# for key, value in data.items():
#     print(key+':', value)


# class Person:
#     pantonimic = 'ANTONOVOCH'
#     def __init__(self,lastname,name,age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age


#     def get__full__name(self):
#         return f'{self.lastname} {self.name}'

# man1 = Person('ANTONIO','ANTONIO DE MAKARONE',14)
# print(man1.name)
# print(man1.lastname)
# print(man1.age)

# print('########################')

# another_man2 = Person()
# print(another_man2.name)
# print(another_man2.lastname)
# print(another_man2.age)

# print(id(man1), id(another_man2))


# базовая конструкция для создания класса:
# ключевое слово "class" + название класса с большой буквы
# class NameClass:
#     # создание свойств, одинаковых для всех
#     # color = 'красный'
#     # memory = 256
#     # camera = 105
#     def init(self, color, gb, mpx):
#         # метод ИНИЦИАЛИЗАЦИИ экземпляра класса.
#         # он запускается в момент создания экземпляра и позволяет
#         # для каждого объекта передать и задать уникальные свойства.
#         print('Я создался')
#         # self -> это обращение к объекту изнутри, "внутри себя"
#         self.color = color
#         self.memory = gb
#         self.camera = mpx
#         print(self.color, self.memory, self.camera)

#     def str(self):
#         # машический метод, который учит
#         # объекты этого класса выводиться в консоль.
#         # Обязательно ВЕРНУТЬ значение!!!
#         return self.color

#     def eq(self, anower_obj):
#         # метод, который учит объект работать с оператором "=="
#         if self.camera == anower_obj.camera and self.color == anower_obj.color and self.memory == anower_obj.memory:
#             return True
#         return False

# # создаем экземпляры класса NameClass с указанными свойствами,
# # которые передаются в init
# obj = NameClass('синий', 128, 56)
# # obj = NameClass('красный', 64, 56)
# obj1 = NameClass('красный', 64, 56)

# print(obj == obj1)


# class Person:
#     pantonimic = 'ANTONOVOCH'
#     def __init__(self,lastname,name,age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#     def __str__(self):
#         return f'{self.lastname} {self.name} {self.age} лет(год(а)).'
#     def greet(self):
#         print(f"hallo! My name is {self.lastname},me {self.age} age")
# man = Person('ANTONIO','ANTONIO DE MAKARONE',14)
# man.greet()


# class Person:
#     def __init__(self,lastname,name,age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.grades = []
#     def __str__(self):
#         return f'{self.lastname} {self.name} {self.age} лет(год(а)).'
#     def greet(self):
#         print(f"hallo! My name is {self.lastname},me {self.age} age")
#     def add_grade(self,grade):
#         self.grades.append(grade)
#     def get_average(self):
#         return sum(self.grades) / len(self.grades)
# student = [
#     Person('Nikita','Ivan',15),
#     Person('Vorsin','Misha',15),
#     Person('MIDAL','Leha',15),
#     Person('ALEKS','Ivan',15)
# ]
# from random import randint
# for stud in student:
#     for i in range(7):
#         stud.add_grade(randint(2,5))

# student.sort(key=lambda stud: stud.get_average(),reverse = True)
# for stud in student:
#     print(stud,'|',f'средний балл:',round(stud.get_average(),2))


# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# class Record:
#     def __init__(self,pt1,pt2):
#         self.pon1 = pt1
#         self.pon2 = pt2
#     def get_area(self):
#         a = abs(self.pon1.x - self.pon2.x)
#         b = abs(self.pon1.y - self.pon2.y)
#         return a * b
#     def get_perimetr(self):
#         a = abs(self.pon1.x - self.pon2.x)
#         b = abs(self.pon1.y - self.pon2.y)
#         return  (a + b) * 2
#     def has_point(self, point):
#         result_x = max([self.pon1.x, self.pon2.x]) >= point.x >= min([self.pon1.x, self.pon2.x])
#         result_y = max([self.pon1.y, self.pon2.y]) >= point.y >= min([self.pon1.y, self.pon2.y])
#         if result_x and result_y:
#             return True
#         return False
# pon1 = Point(1,3)
# pon2 = Point(3,1)
# rect = Record(pon1,pon2)
# print(rect.get_area())
# rect = Record(Point(10, 45), Point(-35, -23))
# print(rect.get_area())
# print(rect.get_perimetr())
# print(rect.has_point(Point(-37, -23)))

# class Person:
#     human_class = 'Хомосапиенс'
#     def __init__(self, name, sername, age):
#         self.name = name
#         self.__sername = sername
#         self._age = age

#     def __get_age(self):
#         print(self.__age)
# man = Person('Никита', 'Тургеньев', 14)
# print(man.__sername)


# class car:
#     __angin_status = False
#     def __init__(self, color,tip,year):
#        self.__color = color
#        self.__tip = tip
#        self.__year = year
#     def start_angin(self):
#         if self.__year >= 2009 :
#             print('Двигатель заведен')
#         else:
#             print('Двигатель уже заведен ')
#             self.__angin_status = True
#     def stop_angin(self):
#         if self.__angin_status:
#             print('Двигатель заглушен')
#             self.__angin_status = False
#         else:
#             print('Двигатель заглушен')
# def change_year(self, year):
#     self.__year = year
# def change_tip(self, tip):
#     self.__tip = tip
# def change_color(self, color):
#     self.__color = color
# def __str__(self):
#     return f'Автомобиль{self.__year} года, {self.__color} цвета "{self.__tip}".'
# haval = car('blue',2022,'croccower')
# haval.change_year(2022)
# haval.change_tip("redan")
# haval.change_color("blue")
# print(haval)
# rav = car('white','4',2009)
# rav.start_angin()
# rav.stop_angin()
# rav.start_angin()


# import string
# class Alphabet:
#     def __init__(self,lang,lets):
#         self.__language = lang
#         self.__letters = lets
#     def __str__(self):
#         return f'language: {self.__language}, letters: {self.__letters}'
# abc = Alphabet('eng',string.ascii_letters)
# print(abc)


# print('здравия желаю верховный главный командающий')
# print('введите год автомобиля')
# a = int(input())
# print('введите тип автомобиля')
# b = input()
# class Car:
#     def __init__(self,year, mark, model):
#        self.year = year
#        self.mark = mark
#        self.model = model
#     def __str__(self):
#         return f'Автомобиль{self.__year} года, {self.__color} цвета "{self.__tip}".'
# cars = [
#     Car(2017,'Audi','A8'),
#     Car(2019,'Audi','A4'),
#     Car(2018,'Audi','A5'),
#     Car(2016,'Audi','S'),
#     Car(2020,'Audi','D'),
#     Car(2002,'ford','CUSTUM1'),
#     Car(2019,'ford','CUSTUM2'),
#     Car(2021,'ford','CUSTUM12'),
#     Car(2022,'ford','CUSTUM14'),
#     Car(2023,'ford','CUSTUM15'),
#     Car(2008,'BMW','M7'),
#     Car(2009,'BMW','M8'),
#     Car(2010,'BMW','2'),
#     Car(2011,'BMW','1'),
#     Car(2022,'BMW','M2'),
#     Car(2013,'KIA','RIO'),
#     Car(2015,'KIA','K8'),
#     Car(2011,'KIA','K5'),
#     Car(2012,'KIA','Cerato'),
#     Car(2020,'KIA','K900'),
#     Car(2017,'Audi','A100'),
#     Car(2019,'Audi','A13'),
#     Car(2018,'Audi','A15'),
#     Car(2016,'Audi','Sg'),
#     Car(2020,'Audi','Df'),
#     Car(2002,'ford','CUSTUM15'),
#     Car(2019,'ford','CUSTUM23'),
#     Car(2021,'ford','CUSTUM122'),
#     Car(2022,'ford','CUSTUM13'),
#     Car(2023,'ford','CUSTUM5'),
#     Car(2008,'BMW','M7'),
#     Car(2009,'BMW','M15'),
#     Car(2010,'BMW','13'),
#     Car(2011,'BMW','18'),
#     Car(2022,'BMW','M22'),
#     Car(2013,'KIA','RIOn'),
#     Car(2015,'KIA','K1'),
#     Car(2011,'KIA','K8'),
#     Car(2012,'KIA','Ceraton'),
#     Car(2020,'KIA','K9000')
# ]
# for car in cars:
#     if a == car.year and b == car.mark:
#         print('по вашему запросу были найдены:',car.year, car.mark, car.model)
#         print('большую информацию вы можете найти здесь:','https://auto.mail.ru/catalog/')
# print('если что-то не работает, то возможно вы непрвельно ввели год или тип автомобиля ну или просто я делал это на скорую руку')
# print('введите код разработчика что бы изменить информацию')
# a23 = int(input())
# if a23 == 2002:
#    print('введите новый год автомобиля:')
#    a24 = int(input())
#    print('введите новую марку автомобиля:')
#    a25 = int(input())
#    print('введите новую модель автомобиля:')
#    a26 = int(input())

# def change_year(self, year):
#         self.__year = a24
# def change_mark(self, mark):
#         self.__mark = a25
# def change_tip(self, tip):
#         self.__tip= a26


# class Person:
#     def __init__(self, name):
#         self.Name = name
#         self.__CardNumber = 4444
#     def count(self, ch1, ch2):
#         return ch1+ch2
#     def GetLastDigit(self):
#         return self.__CardNumber % 10
#     def GetAge(self):
#         return 12
#     def DoubleAge(self):
#         return self.__GetAge() * 2

# a = Person("Timofey")
# print(a.GetLastDigit())
# print(a.DoubleAge())


# import random
# class Mob:
#     def __init__(self, name):
#         self.__level = 1
#         self.__name = name
#         self.__hp = 10
#         self.__attack = 2
#         self.__agility = 1
#         self.__armor = 0
#     def GetDamage(self):
#         return random.randint(self.__attack, self.__attack*2)
#     def SufferDamage(self, dmg):
#         self.__hp -= dmg
#         return self.__hp > 0
#     def LevelUP(self):
#         self.__level += 1
#         self.__hp = 10*self.__level

# player = Mob("Крипер")
# enemy = Mob("Зомби")
# while True:
#     dmg = player.GetDamage()
#     print(player.name, "взорвался", enemy.name,"на", dmg)
#     if not enemy.SufferDamage(dmg):
#         player.LevelUP()
#         enemy = Mob("Зомби")
#         print(player.name, "победил. Идём дальше...")
#         continue
#     dmg = enemy.GetDamage()
#     print(enemy.name,"ударил",player.name, "на",dmg)
#     if not player.SufferDamage(dmg):
#         print(enemy.name, "победил")
#         break


# class Lightsaber:
#     def __init__(self, color):
#         self.__color=color
#         self.__lenght=80
#         self.__blades=1
#         self.__turned=False
#     def ToggleTurn(self):
#         self.__turned = not self.__turned
#         if self.__turned == True:
#             print('меч зажжён')
#         else:
#             print('меч потушен')
#     def ChangeLength(self, newlength):
#         self.__lenght = newlength
#         if self.__lenght < 10:
#             self.__lenght = 10
#         print(f"меч поменялся до {newlength}см и стал {self.__length}см")
#     def ChangeColor(self, newcolor):
#             Colors = ['красный','синий','зелёный','жёлтый','фиолетовый','белый']
#             if newcolor in Сolors:
#                 self.__color = newcolor
#             print(f"цвет меча: {self.__color}")

# b = Lightsaber("Синий")
# b.ToggleTurn()
# b.ChangeLength(50)
# b.ChangeColor("белый")


# class simcard:
#     def __init__(self, phonenumber):
#         self.__number = phonenumber
#         self.__Enable = True
#         self.__TarifName = "Безлемит"
#         self.__TarifPrice = 600
#         self.__Balance = 0
#     def Activata(self):
#         self.__Enable = not self.__Enable
#         if self.__Enable:
#             print('Сим-карта включена')
#         else:
#             print('сим-карта выключена')
#     def ChangeTarif(self, newName, newPrice):
#         self.__TarifName = newName
#         self.__TarifPrice = newPrice
#         print("Новый тариф: {self.__TarifName} по цене {self.__TarifPrice}руб/месяц")
#     def  ChangeBalance(self, change):
#         self.__Balance += change
#         print(f'Новый баланс: {self.__Balance}')
# d = simcard("+79998887652")
# d.Activate()
# d.ChangeTarif("Новый", 100)
# d.ChangeBalance(-100)


# class Rectangle:
#     def __init__(self,pt1,pt2):
#        self.point_1 = pt1
#        self.point_2 = pt2
#        print(1,self)
#     def get_area(self):
#         a = abs(self.point_1.x - self.point_2.x)
#         return
#     def get_perimetr(self):
#         return
# rect = Rectangle((3,1),(2,5))
# print(2,rect)
# print('-'*20)
# rect2 = Rectangle((3,1),(2,5))
# print(2,rect2)


# class Rectangle:
#     def __init__(self,pt1,pt2):
#        self.point_1 = pt1
#        self.point_2 = pt2
#        print(1,self)
#     def get_area(self):
#         a = abs(self.point_1.x - self.point_2.x)
#         return
#     def get_perimetr(self):
#         return
# rect = Rectangle((3,1),(2,5))
# rect.get_area()
# Rectangle.get_area(rect)


# class  Home:
#     def __init__(self,_area,_price):
#        self.area = _area
#        self.price =_price

# class  Man:
#     def __init__(self,name, age, money, home):
#        self.__name = name
#        self.__age = age
#        self.__money = money
#        self.__home = home

#     def buy_house(self,house):
#         if a2 >= self.__age and self.__money >= house.price and self.__home:
#             self.__money -= house.price
#             print('остаток:',self.__money)
#             print('дом куплен поздравляем')
#         if c1 == True:
#             print('у вас уже есть дом')
#         if self.__money < house.price:
#             print('мы можем зделать вам скидку 1000р')
#         house.price -= 1000
#         print(house.price)
#         if self.__money < house.price:
#             print('вам все еще не хватает')
#             print('пойти на работу или нет(ответ либо да или нет)')
#             c2 = input()
#             if c2 == 'да':
#                c2  = True
#             else:
#                c2 = False
#             if c2 == True:
#               self.__money +=9000
#         else:
#             print('проблемы EEEEGGNORRR FILE OLDER')
# print('регистрация')
# print('предоставте пожалуйста свою информацию')
# a1 = input()
# print('1.Номер телефона(только цыфры):')
# a2 = int(input())
# print('введите год рождения')
# a = int(input())
# print('введите Имя:')
# b =  input()
# print('введе свое наличие денег(любое число без букв):')
# c = int(input())
# print('введите есть ли у вас жилье (да,нет):')
# c1 = input()
# if c1 == 'да':
#    c1 = True
# else:
#    c1= False
# dom = Home(100,10000)

# man = Man(b, a, c, c1)
# man.buy_house(dom)
# man.buy_house(dom)
# man.buy_house(dom)
# man.buy_house(dom)
# man.buy_house(dom)
# man.buy_house(dom)
# man.buy_house(dom)
# man.buy_house(dom)
# man.buy_house(dom)
# man.buy_house(dom)
# man.buy_house(dom)
# man.buy_house(dom)


# from  easygui  import
# class  Home:
#     def __init__(self,_area,_price):
#        self.area = _area
#        self.price =_price

# class  Man:
#     def __init__(self,name, age, money, home):
#        self.__name = name
#        self.__age = age
#        self.__money = money
#        self.__home = home

#     def buy_house(self,house):
#         if a2 >= self.__age and self.__money >= house.price and self.__home:
#             self.__money -= house.price
#             msgbox ('остаток:',self.__money)
#             msgbox ('дом куплен поздравляем')
#         if c1 == True:
#             msgbox ('у вас уже есть дом')
#         if self.__money < house.price:
#             msgbox ('мы можем зделать вам скидку 1000р согласны?(да или нет)')
#             c3 = multenterbox('\n\n')
#             if c3 == 'да':
#                c3  = True
#             else:
#                c3 = False
#             if c3 == True:
#                house.price -= 1000
#         msgbox ('цена после скидки составляет:',house.price)
#         if self.__money < house.price:
#             msgbox ('вам все еще не хватает')
#             msgbox ('пойти на работу или нет(ответ либо да или нет)')
#             c2 = multenterbox('\n\n')
#             if c2 == 'да':
#                c2  = True
#             else:
#                c2 = False
#             if c2 == True:
#               self.__money +=9000
#         else:
#             msgbox ('проблемы EEEEGGNORRR FILE OLDER')
# msgbox ('регистрация')
# msgbox ('предоставте пожалуйста свою информацию')
# a1 = multenterbox('\n\n')
# msgbox ('1.Номер телефона(только цыфры):')
# a2 = multenterbox('\n')
# msgbox ('введите год рождения')
# a = multenterbox('\n')
# msgbox ('введите Имя:')
# b =  multenterbox('\n\n')
# msgbox ('введе свое наличие денег(любое число без букв):')
# c = multenterbox('\n')
# msgbox ('введите есть ли у вас жилье (да,нет):')
# c1 = multenterbox('\n\n')
# if c1 == 'да':
#    c1 = True
# else:
#    c1= False
# dom = Home(100,10000)
# man = Man(b, a, c, c1)
# man.buy_house(dom)
# man.buy_house(dom)
# man.buy_house(dom)

# import json
# class User:
#     def __init__(self,login,password,name,lastname):
#         self.login = login
#         self.password = password
#         self.name = name
#         self.lastname = lastname
#         self.subscribtion = []
#         self.flowers = []
#     def __repr__(self):
#         return f'User(login = {self.login},password={self.password},name={self.name},lastname={self.lastname})'
#     def subscribe(self,other):
#         self.subscribtion.append(other.login)
#         other.flowers.append(self.login)
#     def info(self):
#         return f" login: {self.login},name: {self.name},lastname: {self.lastname},subscribtion: {len(self.subscribtion)},{len(self.login)*'='})"

# file = open("user.json","r")
# data = json.load(file)
# file.close()
# users = []
# for item in data:
#     users.append(User(item['login'], item['password'],item['name'],item['lastname']))
# current_user = users[0]
# i = 0
# while True:
#     print('-' * 25)
#     print()
#     user = users[i]
#     print(user.info())
#     print()
#     action = input(
#     f'Действия: \n'
#     f'1)подписаться: \n'
#     f'2)следуйщий: \n'
#     f'3)выйти: \n'
#     f'>> '

# )
#     if action == '1':
#        current_user.subscribe(user)
#        print(f'вы подписались на:{user.login}')
#     if action == '3':
#         break
#     i +=1
#     if i == len(users):
#         i=0


# print('ведите цвета для смешивания')
# print('1 цвет')
# a = input()
# print('2 цвет')
# b = input()
# if a == 'красный' and a =='желтый' and a =='синий':
#    print('ошибка. выберите другой цвет тк эти цвета не смешиваются')
# elif b == 'красный'and b =='желтый'and b =='синий':
#    print('ошибка. выберите другой цвет тк эти цвета не смешиваются')
# elif a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
#     print('фиолетовый')
# elif a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
#     print('оранжевый')
# elif a == 'синий' and b == 'желтый' or b == 'синий' and a == 'желтый':
#     print('зеленый')
# elif a =='красный' and b =='красный':
#     print('красный')
# elif a =='синий' and b =='синий':
#     print('синий')
# elif a =='желтый' and b =='желтый':
#     print('желтый')
# else:
#    print('ошибка. выберите другой цвет тк эти цвета не смешиваются')


# print('о неn начался зомби апокалипсис')
# print('сколько зомби было к началу расчета:')
# a = int(input())
# print('сколько каждый может заразить:')
# b = int(input())
# print('сколько дней он шел')
# c = int(input())
# for i in range(1, c + 1):
#     print(i,'день',',','зомби:',a,  )
#     a3 = a * b
#     a += a3


# file = open('data.txt')
# print('file name:', file.name)
# a = 0
# b = 0
# c = 0
# for line in file:
#     a += 1
#     b += len(line.split())
#     c += len(line.strip('\n'))
# print("строк:", a)
# print("слов:", b)
# print("символов:", c)


# print('введите фразу:')
# a = input()
# str.split(sep=None, maxsplit=-1)
# s = a
# print(f'List of Words ={s.split()}')
# def add_time_delta(h, m, delta):
#     new_n = (m + delta) % 60
#     new_h = h + ((m + delta) // 60)
#     return new_h, new_n
# time_start = '8:00'
# lesson_duration = 45
# break_duration = 18
# count_lessons = 4
# time_list = time_start.strip().split(':')
# h = int(time_list[0])
# m = int(time_list/[1])
# for lesson_num in range(1, count_lessons + 1):
#     h_new, n_new = add_time_delta(h, m, lesson_duration)
#     print (f'Урок %{lesson_num}: {h:02}:{m:02} - {h_new:02}:{n_new:02}')
#     h_new, m_new = add_time_delta(h_new, m_new, break_duration)
#     h, m = h_new, n_new

# a = [int(i) for i in input().split()]
# b = str(a[0])
# j = int(len(a) - 1)
# c = str(a[j])
# a1 = [int(c),int(b)]
# a1.insert(1,a)
# s = 0
# print(b)
# print(c)
# print(type(b))
# print(a1)
# for i in range(1, len(a1) - 1):
#     s = a1[i - 1] + a1[i + 1]
#     print(s, end=' ')

# def sum_num(nums):
#     nums = list(map(int,nums.split()))


# class Pen:
#     def __init__(self,color):
#         self.color = color
# P = Pen()
# color = 'red'
# print(P.color)


# from tkinter import*
# root = Tk() #главный экран
# #--------------------------- Кнопка обычная ----------------------
# def click_btn():
#     btn['text'] = 'тепреь я нажатая кнопка'
#     print('button нажат')
# btn = Button(root, text='button',width=20, height = 2,command = click_btn)
# btn.pack()
# root.mainloop()# запуск основного програмного цикла


# from tkinter import *


# root = Tk() # создаем главный экран

# # ---------------------- Кнопка обычная ----------------------
# def click_btn():
#     btn['text'] = 'Я нажатая кнопка'
#     print('Кнопка нажата')

# btn = Button(root, text='Я кнопка', width=20, height=2, command=click_btn)
# btn.pack()

# # ------------------------- Кнопка через КЛАСС -------------------------
# class MyButton:
#     def __init__(self, window, text, cmd):
#         self.btn = Button(window)
#         self.btn['text'] = text
#         self.btn['command'] = cmd
#         self.btn['width'] = 20
#         self.btn['height'] = 2
#         self.btn.pack()

# def click_btn():
#     print('Кнопка нажата')

# btn1 = MyButton(root, 'Я кнопка 1', click_btn)
# btn2 = MyButton(root, 'Я кнопка 2', click_btn)

# # ---------------------- Надпись == Метка == Label ----------------------
# label = Label(root,
#               text='Супер метка',   # текст надписи
#               fg='red',             # цвет текста
#               bg='black',           # цвет фона
#               font='consolas 18'    # шрифт и размер
#               )
# label.pack()

# def change_label():
#     label['text'] = 'Кнопочка ниже была нажата'

# btn_label = MyButton(root, 'Кнопка для текста выше', change_label)

# # --------------------- Однострочное поле для ввода ---------------------
# entry_input = Entry(root, width=30, font='consolas 18')
# entry_input.pack()

# def get_value():
#     label['text'] = entry_input.get()
#     print(entry_input.get())

# entry_input_btn = MyButton(root, 'получить ввод', get_value)

# #---------------------Многострочное поле для ввода-------------
# text_input = Text(root,width=30,height=20,font='consolas 18')
# text_input.pack()
# def get_text_value():
#     print(text_input.get('1.0',END))
# text_input_btn = MyButton(root,'получить ввод текста', get_text_value)
# # --------------------- Радиокнопки (переключатели) ---------------------
# var = IntVar(value=1)
# radio_btn_1 = Radiobutton(root, text='вариант 1', variable=var, value=1)
# radio_btn_2 = Radiobutton(root, text='вариант 2', variable=var, value=2)
# radio_btn_3 = Radiobutton(root, text='вариант 3', variable=var, value=3)
# radio_btn_1.pack()
# radio_btn_2.pack()
# radio_btn_3.pack()
# #-------------------Чекбоксы(флажки)------------
# check_var_1 = IntVar()
# check_var_2 = IntVar()
# check_btn_1 = Checkbutton(root, text = 'flag 1', variable=check_var_1,onvalue=1,offvalue=2)
# check_btn_2 = Checkbutton(root, text = 'flag 2', variable=check_var_2,onvalue=0,offvalue=5)
# # выще перемнные запоминающие текущие состояние
# check_btn_1.pack()
# check_btn_2.pack()
# #----------------------------- Списски-------------
# languages = ['Python','Pascal','c++','c','c#','basic','1C','java','java script']
# list_variants = Variable(value=languages)
# langs_list = Listbox(root,selectmode=SINGLE,height=4,listvariable=list_variants)
# langs_list.pack()
# root.mainloop() # запуск основного програмного цикла


# from tkinter import *

# root = Tk()

# class ColorButton:
#     colors = {
#         'красный': '#ff0000',
#         'оранжевый': '#ff7d00',
#         'желтый': '#ffff00',
#         'зеленый': '#00ff00',
#         'голубой': '#007dff',
#         'синий': '#0000ff',
#         'фиолетовый': '#7d00ff',
#     }

#     def __init__(self, win, color_name, label, entry_var):
#         self.color_name = color_name                # название цвета
#         self.color_code = self.colors[color_name]   # код цвета
#         self.label = label
#         self.entry_var = entry_var

#         self.btn = Label(
#             win, text='', width= 30, height=3, bg=self.color_code
#         )
#         self.btn.bind('<Button-1>', self.change_label)
#         self.btn.pack()


#     def change_label(self, event):
#         self.label['text'] = self.color_name
#         self.entry_var.set(self.color_code)

# label = Label(root, text='красный', font='arial 18')
# label.pack()

# str_var = StringVar(value=ColorButton.colors['красный'])
# entry = Entry(root, width=30, textvariable=str_var, justify='center', font='arial 18')
# entry.pack()

# btn1 = ColorButton(root, 'красный', label, str_var)
# btn2 = ColorButton(root, 'оранжевый', label, str_var)
# btn3 = ColorButton(root, 'желтый', label, str_var)
# btn4 = ColorButton(root, 'зеленый', label, str_var)
# btn5 = ColorButton(root, 'голубой', label, str_var)
# btn6 = ColorButton(root, 'синий', label, str_var)
# btn7 = ColorButton(root, 'фиолетовый', label, str_var)

# root.mainloop()


# from tkinter import *
# CONSOLAS = 'Consolaas 18'
# root = Tk()
# btn1 = Button(root,text='1', font=CONSOLAS, width=20, height=3)
# btn2 = Button(root,text='2', font=CONSOLAS, width=20, height=3)
# btn3 = Button(root,text='3', font=CONSOLAS, width=20, height=3)
# btn4 = Button(root,text='4', font=CONSOLAS, width=20, height=3)
# btn1.pack(side=TOP)
# btn2.pack(side=LEFT)
# btn3.pack(side=RIGHT)
# btn4.pack(side=BOTTOM)
# root.mainloop()


# from tkinter import *
# CONSOLAS = 'Consolaas 18'
# root = Tk()
# row1 = Frame(root)
# row2 = Frame(root)
# btn1 = Button(row1,text='1', font=CONSOLAS, width=20, height=3)
# btn2 = Button(row1,text='2', font=CONSOLAS, width=20, height=3)
# btn3 = Button(row2,text='3', font=CONSOLAS, width=20, height=3)
# btn4 = Button(row2,text='4', font=CONSOLAS, width=20, height=3)
# row1.pack(side=TOP,pady=10)
# row2.pack(side=BOTTOM,pady=10)
# btn1.pack(side=LEFT,padx=5)
# btn2.pack(side=LEFT,padx=5)
# btn3.pack(side=LEFT,padx=5)
# btn4.pack(side=LEFT,padx=5)
# root.mainloop()


# from tkinter import *
# CONSOLAS = 'Consolaas 18'
# root = Tk()
# fill_btn = Button(root,text='меня бьют ногами в лицо', font=CONSOLAS, width=20, height=3)
# fill_btn.pack(
#     expand=1,
#     fill=BOTH
# )
# row1 = Frame(root,bg='red')
# row2 = Frame(root,bg='blue')
# btn1 = Button(row1,text='1', font=CONSOLAS, width=20, height=3)
# btn2 = Button(row1,text='2', font=CONSOLAS, width=20, height=3)
# btn3 = Button(row2,text='3', font=CONSOLAS, width=20, height=3)
# btn4 = Button(row2,text='4', font=CONSOLAS, width=20, height=3)
# row1.pack(side=TOP,ipady=10,expand=1,fill=BOTH)
# row2.pack(side=BOTTOM,ipady=10,expand=1,fill=BOTH)
# btn1.pack(side=LEFT,padx=5,expand=1,fill=BOTH)
# btn2.pack(side=LEFT,padx=5,expand=1,fill=BOTH)
# btn3.pack(side=LEFT,padx=5,expand=1,fill=BOTH)
# btn4.pack(side=LEFT,padx=5,expand=1,fill=BOTH)
# root.mainloop()


# from tkinter import *
# root = Tk()
# CONSOLAS = 'Consolaas 18'
# textarrea = Text(root, font=CONSOLAS, padx=5,pady=5)
# scroll = Scrollbar(command=textarrea.yview)
# textarrea.config(yscrollcommand=scroll.set)
# def get():
#     text = textarrea.get('1.0',END)
#     print(123)
# btn_get = Button(root,text='Меня бьют ногами в лицо',command=get)

# def insert():
#     text = 'ффххфхфхфхфхфхфхфахахха меняяяя бьююют ногами в лицо ахахах офникии хахах думая что чвк редан ахаххаха но они не знают что я мертв внутриааххахаха*'
#     textarrea.insert(END, text)
# btn_insert = Button(root,text='Меня бьют ногами в лицо',command=insert)

# textarrea.pack(side=LEFT,expand=1,fill=BOTH)
# scroll.pack(side=LEFT,expand=1,fill=Y)
# btn_get.pack(side=LEFT, padx=5, pady=5, fill=Y)

# btn_insert.pack(side=LEFT, padx=5, pady=5, fill=Y)

# root.mainloop()

# from tkinter import *

# root = Tk()

# class ColorButton:
#     colors = {
#         'красный': '#ff0000',
#         'оранжевый': '#ff7d00',
#         'желтый': '#ffff00',
#         'зеленый': '#00ff00',
#         'голубой': '#007dff',
#         'синий': '#0000ff',
#         'фиолетовый': '#7d00ff',
#     }

#     def __init__(self, win, color_name, label, entry_var):
#         self.color_name = color_name                # название цвета
#         self.color_code = self.colors[color_name]   # код цвета
#         self.label = label
#         self.entry_var = entry_var

#         self.btn = Label(
#             win, text='', width= 30, height=3, bg=self.color_code
#         )
#         self.btn.bind('<Button-1>', self.change_label)
#         self.btn.pack(side=LEFT)
#     def change_label(self, event):
#         self.label['text'] = self.color_name
#         self.entry_var.set(self.color_code)
# label = Label(root, text='красный', font='arial 18')
# label.pack()
# str_var = StringVar(value=ColorButton.colors['красный'])
# entry = Entry(root, width=30, textvariable=str_var, justify='center', font='arial 18')
# entry.pack()
# btn1 = ColorButton(root, 'красный', label, str_var)
# btn2 = ColorButton(root, 'оранжевый', label, str_var)
# btn3 = ColorButton(root, 'желтый', label, str_var)
# btn4 = ColorButton(root, 'зеленый', label, str_var)
# btn5 = ColorButton(root, 'голубой', label, str_var)
# btn6 = ColorButton(root, 'синий', label, str_var)
# btn7 = ColorButton(root, 'фиолетовый', label, str_var)

# root.mainloop()


# from tkinter import *
# CONSOLAS = 'Consolas 16'
# root = Tk()
# header = Frame(root)
# label= Label(header,text='file_name:',font=CONSOLAS)
# file_name_input = Entry(header, font=CONSOLAS)
# def file_open():
#     file_name = file_name_input.get()
#     file = open(file_name,'r',encoding='UTF-8')
#     data = file.read()
#     file.close()
#     textarea.insert('1.0',END)
#     textarea.insert('1.0',data)
# btn_open = Button(header, text='open',command=file_open, width=20)
# def file_save():
#     file_name = file_name_input.get()
#     file = open(file_name,'w',encoding='UTF-8')
#     data = textarea.get('1.0',data)
#     file.write(data)
#     file.close()
# btn_save = Button(header,text='save',command=file_save,width=20)
# btn_save = Button(header, text='save',command=file_open, width=20)
# body = Frame(root)
# textarea= Text(body, font=CONSOLAS)
# scroll_y=Scrollbar(body,command=textarea.yview)
# textarea.config(yscrollcommand=scroll_y.set)
# scroll_x= Scrollbar(root, command=textarea.xview,orient='horizontal')
# textarea.config(sxscrollcommand=scroll_x.set)
# header.pack(fill=X, padx=5, ipady=5)
# body.pack(expand=1, fill=BOTH, ipadx=5, ipady=5)
# file_name_input.pack(expand=1, fill=X, side=LEFT)
# btn_open.pack(side=LEFT, padx=5)
# btn_save.pack(side=LEFT)
# textarea.pack(expand=1, fill=BOTH, side=LEFT)
# scroll_y.pack(expand=1, fill=Y, side=LEFT)
# root.mainloop()

##
#
#
##  2 ГОД
#
#
##

# a = input()
# a = a+','+a+','+a
# print(a)


# a = input()
# print(a[0])
# print(a[-1])
# if len(a) % 2 >= 1:
#     n =len(a) // 2
#     print(a[n])


# a = input()
# if len(a) > 5:
#     print (a[0:3])
#     print (a[-3:-1])
# else:
#     print((a[0]*len(a)))


# a = list(input())
# b = ['0','1','2','3','4','5','6','7']
# c = []
# for i in a:
#    for q in b:
#     if i == q:
#         c.append(i)
# print(*c,sep=', ')


# a = input()
# print(a[::3])

# c = ['www']
# b = ['zzz']
# a = input()
# v = a.split()
# if a[0:3] =='abc':
#    v.clear()
#    v.extend(c)
#    v.join()
#    print(v)
# else:
#     print(a + 'zzz')

# a = input()
# if a[0:3] =='abc':
#    a = a.replace('abc', 'www')
#    print(a)
# else:
#     print(a + 'zzz')


# a = input()
# a_str = str(a)
# b = len(a_str)


# # начаьное количество
# a = int(input())
# # процент увелечения
# b = int(input())
# #дни
# c = int(input())
# for i in range(1,c+1):
#     print(i,'день',',','людей:',a)
#     a2 = (a/100) * b
#     a3 = a + a2
# print('итог людей за',c,'дней','равен:', a3)

# 2 год 2 год
# a=input()
# a=a+','+a+","+a
# print(a)

# a=input()
# d=(len(a))
# if d%2==0:
#   print(a[0],a[-1])
# else:
#   print(a[0],a[d/2],a[d])

# a=input()
# print(a[::3])

# a=input()

# if a[0:3]=="abc":
#     print(a.replace('abc',"www",1))
# else:
#     print(a+'zzz')

# s=input()
# num=list()
# for char in s:
#     if char.isnumeric():
#         num.append(char)
# print(num)

# from random import *
# a=int(input())
# while True:
#     s=randint(1,6)
#     if a!=s:
#         print("повезло")
#     else:
#         print("конец")
#         break

# for i in range (6):
#     a=int(input())
#     b=randint(1,6)
#     if a==b:
#         print("end")
#     else:
#         print("nice")
# from statistics import *

# a=list(map(int,input().split(" ")))

# s=sum(a)/len(a)
# for i in a:
#     if i>s:
#         print(i)

# list = [-i for i  in a]

# a=list(input())
# a[0], a[-1] = a[-1], a[0]

# n=5
# for _ in range (len(a)//n):
#     print([i for i in a[n*_:n(_+1)]])

# for i in range(len(a)):
#     r=choice(a)
#     del a[a.index(r)]
#     print(r)

# print(type(a))

# a=1
# def func(something):
#     something=list(map(int,input().split()))
#     s=sorted(something)
#     return s
# b=func(a)
# print(b)

























































































































































































































































































































































































































































































































































































































































































































































































































































