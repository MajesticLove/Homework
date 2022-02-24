#1
name = 'егор'
print(name)

#2
age = 19
print('я есть егор, мне ', age, 'лет')

#3
name5 = name*5
print(name5)

#4
print('потребуется твоё имя и твой возраст')
name_u = input()
age_u = input()
print('привет, ', name_u, 'тебе не ' + age_u + '. шучу)))')

#5
age_u = int(age_u)
if age_u < 18:
    print('привет, малыш')
if age_u >= 18 or age_u <= 36:
    print('совсем взрослый')

#6
print(name_u[1:-1])
print(name_u[::-1])
print(name_u[-3:])
print(name_u[:5])

#7
a_name = len(name_u)
print(a_name)
print('cумма цифр возраста', age_u % 10 + age_u // 10)
print('произведение цифр возраста', age_u % 10 * age_u // 10)


#8
print(name_u.lower())
print(name_u.upper())
print(name_u.lower()[0] + name_u[1:])
print(name_u.upper()[0] + name_u[1:])

#9
user_age_str = input('ваш возраст: ')
try:
    user_age_int = int(user_age_str)
    if int(user_age_str) > 0 and int(user_age_str) <= 150:
        print('ваш возраст: ', user_age_int)
        user_name = input('ваше имя: ')
        try:
            user_name = str(user_name)
            if ' ' in user_name:
                print('введите имя без пробелов')
            else:
                print('ваше имя: ', user_name)
        except:
            print('имя должно состоять из букв и не содержать пробелы')
    else:
        print('недопустимый возраст')
except:
    print('необходимо ввести числовое значение')


#10
answer = int(input("Сколько будет 4*5? "))
try:
    answer = int(answer)
    if answer == 20:
        print('верно!!')
    else:
        print('неправильно!!')
except:
    print('необходимо ввести числовое значение')