immutable_var = 1, 2, 3, 'OJ'
print(immutable_var)

# immutable_var[0]= 6 - Невозможно поменять значение в кортеже, потому как он является неизменняемым

mutable_list = ([1, 2, 3, 4, 'OJ'])
print(mutable_list,' - old')
mutable_list [0] = '#'
mutable_list [3] = '$SPB'
mutable_list [4] = 52
print(mutable_list, ' - new')