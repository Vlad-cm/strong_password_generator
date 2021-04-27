#!/usr/bin/env python3

import random
import string
import sys

help_ = '''
This is strong password generator.
Usage: spg.py [OPTION]...
For commands -c, -l transmit an integer together with through a space.
    -h, --help      display this help and exit
    -c              choose the number of passwords to generate    
    -l              choose password length
    -d              whether to take numbers (1/0 or yes/no)
    -lc             whether to take lowercase letters (1/0 or yes/no)
    -uc             whether to take uppercase letters (1/0  or yes/no)
    -s              whether to take punctuation marks (1/0 or yes/no)
    -p              for use human-like requests
'''

params = {
    "count": 1,
    "len": 8,
    "digits": "1",
    "low_case": "1",
    "up_case": "1",
    "special": "1"
}

human_like = False

if ("-h" or "--help") in sys.argv:
    print(help_)
    sys.exit()

if len(sys.argv) > 1:
    if "-c" in sys.argv:
        params.update({"count": int(sys.argv[sys.argv.index("-c") + 1])})
    if "-l" in sys.argv:
        params.update({"len": int(sys.argv[sys.argv.index("-l") + 1])})
    if "-d" in sys.argv:
        params.update({"digits": sys.argv[sys.argv.index("-d") + 1]})
    if "-lc" in sys.argv:
        params.update({"low_case": sys.argv[sys.argv.index("-lc") + 1]})
    if "-uc" in sys.argv:
        params.update({"up_case": sys.argv[sys.argv.index("-ul") + 1]})
    if "-s" in sys.argv:
        params.update({"special": sys.argv[sys.argv.index("-s") + 1]})
    if "-p" in sys.argv:
        human_like = True

digits = '1234567890'
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
special = '!#$%&*+-=?@^_.'

password_list = []
if human_like:
    print('Здравствуйте, я ваш генератор надёжный паролей')
    params.update({"count": int(input('Сколько паролей вам нужно?'))})
    params.update({"len": int(input('Насколько длинный должен быть ваш пароль?'))})
    params.update({"digits": input('Включать ли цифры? (1/0 or yse/no)')})
    params.update({"low_case": input('Включать ли маленькие буквы? (1/0 or yse/no)')})
    params.update({"up_case": input('Включать ли большие буквы? (1/0 or yse/no)')})
    params.update({"special": input('Включать ли знаки пунктуации? (1/0 or yse/no)')})

if params.get("digits") == ("1" or "yes"):
    for a in digits:
        password_list.append(a)
if params.get("low_case") == ("1" or "yes"):
    for b in lowercase_letters:
        password_list.append(b)
if params.get("up_case") == ("1" or "yes"):
    for c in uppercase_letters:
        password_list.append(c)
if params.get("special") == ("1" or "yes"):
    for d in special:
        password_list.append(d)


def generate_password(len_, count):
    password = []
    for i in range(count):
        temp = []
        for j in range(len_):
            temp.append(random.choice(password_list))
        password.append(temp)
    return password


for pass_ in generate_password(params.get("len"), params.get("count")):
    print(*pass_, sep="")

if sys.platform == "win32":
    input()
