
#Попросіть користувача ввести свсвій вік (можно використати константу або input()).

#- якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"

#- якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"

#- якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"

#- якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"

#- у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"



#P.S. На екран має бути виведено лише одне повідомлення! Макож подумайте над варіантами, коли введені невірні дані


user_input = input('Введіть свій вік:')

if user_input.isdigit():
    age = int(user_input)
    if '7' in str(age):
        print("Вам сьогодні пощастить")
    elif age >= 190:
        print('Ви ввели невірні дані')
    elif age == 0:
        print('Ви ввели невірні дані')
    elif age < 7:
        print("Де твої батьки&")
    elif age < 16:
        print("Це фільм для дорослих!")
    elif age > 65:
        print("Покажіть пенсійне посвідчення!")
    else:
        print("А білетів вже немає!")
else:
    print('Ви ввели невірні дані')