#Задача "Счётчик вызовов"
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(a):
    count_calls()
    return len(a), a.upper(), a.lower()

def is_contains(a,b):
    b = [x.lower() for x in b]
    count_calls()
    if a.lower() in b:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(f"колличество вызовов: {calls}")