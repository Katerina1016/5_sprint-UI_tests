from random import randint


class User:
    user_name = 'Екатерина'
    email = 'koroleva.katenka_8_555@yandex.ru '
    password = 'k1603Ol'


class RandomUser:
    user_name = f'name{randint(0, 99)}'
    email = f'mail{randint(0, 99)}@yandex.ru'
    password = f'qw{randint(100, 999)}kat'
