import random

print('Здравствуйте, я ваш генератор надёжный паролей')

digits = '1234567890'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'


print('Сколько паролей вам нужно?')
quantity = int(input())
print('Насколько длинный должен быть ваш пароль?')
length = int(input())
print('Включать ли цифры?[yes/no]')
answer_digits = input()
print('Включать ли маленькие буквы?[yes/no]')
answer_lowercase = input()
print('Включать ли большие буквы?[yes/no]')
answer_uppercase = input()
print('Включать ли знаки пунктуации?[yes/no]')
answer_punctuation = input()


def generate_password(num):
    password_list = []
    for j in range(num):
        password = ''
        for i in range(length):
            if answer_lowercase == 'yes' or answer_lowercase == '1':
                password+=(lowercase_letters[random.randint(0, len(lowercase_letters)-1)])
            if answer_uppercase == 'yes' or answer_uppercase == '1':
                password+=(uppercase_letters[random.randint(0, len(uppercase_letters)-1)])
            if answer_digits == 'yes' or answer_digits == '1':
                password+=(digits[random.randint(0, len(digits)-1)])
            if answer_punctuation == 'yes' or answer_punctuation == '1':
                password+=(punctuation[random.randint(0, len(punctuation)-1)])
        password_list.append(password)

    return password_list


print(*generate_password(quantity))






