my_dict = {'Kirill' : 2000, 'Max' : 2001, 'Kent' : 2052}
print(my_dict, 'Общий словарь')
print(my_dict.get('Kent', "- Вывели, год рождения Кента"))
print(my_dict.get('Gocha', 'Данного имени нет'))

my_dict.update({'agent' : 123,
                'CyberPunk' : 2033})
print(my_dict, 'добавили agent и CyberPunk')

OJ = my_dict.pop('agent')

print(my_dict, 'Удалили agent через pop')
print(OJ, 'вывели его значение')

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
print(my_set, '- исходный Set')
my_set.update((6, 7))
my_set.remove(1)
print(my_set, '- Set после заданий')

