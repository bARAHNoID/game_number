import random

number= random.randint(1,100)

#удалить строку ниже , чтобы не показывало ответ
print (number)

user_number = int(input('введите число...'))
if number==user_number :
    print ('вы угадали, держите пять!')
elif number != user_number and (user_number<100 and user_number>0):
    print (' к сожалению вы не угадали....попробуйте еще раз?!...')
else :
    print('неправильное число, надо выбирать от 1 до 100...')

