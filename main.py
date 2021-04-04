import random

print('Здравствуйте, я ваш генератор надёжный паролей')

digits = '1234567890'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

password_list = []
quantity = int(input('Сколько паролей вам нужно?'))
length = int(input('Насколько длинный должен быть ваш пароль?'))
print('Включать ли цифры?[yes/no]')
answer_digits = input()
if answer_digits == "yes":
    for a in digits:
        password_list.append(a)
print('Включать ли маленькие буквы?[yes/no]')
answer_lowercase = input()
if answer_lowercase == "yes":
    for b in lowercase_letters:
        password_list.append(b)
print('Включать ли большие буквы?[yes/no]')
answer_uppercase = input()
if answer_uppercase == "yes":
    for c in uppercase_letters:
        password_list.append(c)
print('Включать ли знаки пунктуации?[yes/no]')
answer_punctuation = input()
if answer_punctuation == "yes":
    for d in punctuation:
        password_list.append(d)


def generate_password(len, count):
    password = []
    for i in range(count):
        temp = []
        for j in range(len):
            temp.append(random.choice(password_list))
        password.append(temp)
    return password


for passw in generate_password(length, quantity):
    print(*passw, sep="")
