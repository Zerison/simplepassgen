import subprocess
import sys
import importlib

def silent_install(module_name, pip_name=None):
    if pip_name is None:
        pip_name = module_name
    try:
        importlib.import_module(module_name)
    except ImportError:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", pip_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
silent_install("secrets")
silent_install("pyperclip")

import secrets
import pyperclip
import os

def generate_password(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password  

print("Генератор паролей")
a = int(input("Введите длину пароля(12-32):"))
if a<12:
    print('Слишком короткий пароль - небезопасно!')
    print('Повторите попытку')
    a = int(input("Введите длину пароля(12-32):"))
if a>32:
    print('Куда столько!')
    print('Повторите попытку')
    a = int(input("Введите длину пароля(12-32):"))

global password 
password = generate_password(a)

print('\nПароль сгенерирован.\n \nВыберите опцию:')
print('1. Просто вывести и скопировать\n2. Записать в файл ( появится на рабочем столе)\n3. Сгенерировать новый пароль\n4. Выход')
b =(int(input('выберите действие:')))

while b!=4:
    if b == 1:
        pyperclip.copy(password)
        print(f"\nСкопировано в буфер обмена.", 
          f'Ваш пароль: \n{password}\n')       
    elif b == 2:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        if not os.path.exists(desktop_path):
            desktop_path = os.path.join(os.path.expanduser("~"), "Рабочий стол")
        file_path = os.path.join(desktop_path, "Сгенерированные Пароли.txt")
        with open(file_path, 'a') as fill:
            fill.write(f'{password}\n')
        print('\nВсе успешно записано!')
        if os.path.exists(file_path):
            print(f'В файл {file_path} добавлена запись:  ""  {password}  ""\n')
        else:
            print(f"Файл создан: {file_path}\n")
    elif b==3:
        a = int(input("Введите длину пароля(12-32):"))
        password = generate_password(a)
        print('\nНовый пароль сгенерирован\n')
    else:
        print('\n######### Ошибка. Недопустимое значение #########\n')
    print('Выберите опцию:')
    print('1. Просто вывести и скопировать\n2. Записать в файл ( появится на рабочем столе)\n3. Сгенерировать новый пароль\n4. Выход')
    b = int(input('выберите действие:'))
