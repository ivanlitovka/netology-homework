import datetime as dt
from decimal import Decimal

# Холодильник пуст:
goods = {}

# Код, который добавляет продукты в словарь goods.

def add(items, title, amount, expiration_date=None):
    if items[title] not in goods:
        title = {}
        print(items[title])
# Добавляем продукт с названием 'Яйца', количество - 10 шт.
add(goods, 'Яйца', Decimal('10'), '2023-9-30')

# Словарь goods должен стать таким:

# {
#     'Яйца': [
#         {'amount': Decimal('10'), 'expiration_date': datetime.date(2023, 9, 30)}
#     ]
# }

# Снова добавляем продукт с тем же названием, количество - 3 шт.
add(goods, 'Яйца', Decimal('3'), '2023-10-15')

# Словарь goods должен стать таким:

# {
#     'Яйца': [
#         {'amount': Decimal('10'), 'expiration_date': datetime.date(2023, 9, 30)},
#         {'amount': Decimal('3'), 'expiration_date': datetime.date(2023, 10, 15)}
#     ]
# }

# Добавляем продукт с названием 'Вода', количество - 2.5 кг
add(goods, 'Вода', Decimal('2.5'))

# Словарь goods должен стать таким:

# {
#     'Яйца': [
#         {'amount': Decimal('10'), 'expiration_date': datetime.date(2023, 9, 30)},
#         {'amount': Decimal('3'), 'expiration_date': datetime.date(2023, 10, 15)}
#     ],
#     'Вода': [
#         {'amount': Decimal('2.5'), 'expiration_date': None}
#     ]
# } 