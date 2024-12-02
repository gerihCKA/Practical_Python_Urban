first = input("введите первое число ")
second = input("введите второе число ")
third = input("введите третье число ")

if first == second == third:
    print("похожих чисел - 3")
elif first == second or first == third or second == third:
    print("похожих чисел - 2")
else:
    print("похожих чисел - 0")