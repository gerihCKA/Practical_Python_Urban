import tkinter as tk

def get_values():
    num1 = int(numbers_entry_1.get())
    num2 = int(numbers_entry_2.get())
    return num1, num2
def delite_insert_answer_entry(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    res = f'{num1 + num2:.3f}'
    delite_insert_answer_entry(res)

def add1():
    num1, num2 = get_values()
    res = f'{num1 - num2:.3f}'
    delite_insert_answer_entry(res)


def add2():
    num1, num2 = get_values()
    res = f'{num1 * num2:.3f}'
    delite_insert_answer_entry(res)


def add3():
    num1, num2 = get_values()
    res = f'{num1 / num2:.3f}'
    delite_insert_answer_entry(res)


window = tk.Tk()

window.title("Калькулятор")
window.geometry("350x350")
window.resizable(False, False)

button_plus = tk.Button(window, text="+", width=3, height=2, command=add)
button_plus.place(x=120, y=200)
button_minus = tk.Button(window, text="-", width=3, height=2, command=add1)
button_minus.place(x=150, y=200)
button_mnoj = tk.Button(window, text="*", width=3, height=2, command=add2)
button_mnoj.place(x=180, y=200)
button_del = tk.Button(window, text="/", width=3, height=2, command=add3)
button_del.place(x=210, y=200)

numbers_entry_1 = tk.Entry(window, width=20)
numbers_entry_1.place(x=120, y=75)
numbers_entry_2 = tk.Entry(window, width=20)
numbers_entry_2.place(x=120, y=125)

answer_entry = tk.Entry(window, width=20)
answer_entry.place(x=120, y=175)

number_1 = tk.Label(window, text="Введите первое число:")
number_1.place(x=120, y=50)
number_2 = tk.Label(window, text="Введите второе число:")
number_2.place(x=120, y=100)

number_answer = tk.Label(window, text="Результат решения:")
number_answer.place(x=120, y=150)


window.mainloop()