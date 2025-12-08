import datetime as dt
from decimal import Decimal


DATE_FORMAT = '%Y-%m-%d'
# Холодильник пуст:
goods = {}

# Код, который добавляет продукты в словарь goods.

def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []

    if expiration_date:
        expiration_date = dt.datetime.strptime(expiration_date, DATE_FORMAT).date()

    items[title].append({
        'amount': amount,
        'expiration_date': expiration_date
    })

def add_by_note(items, note):
    note = note.split(' ')
    if len(note[-1]) != 10:
        expiration_date = None
        title = ' '.join(note[:-1])
        add(items, title, Decimal(note[-1]), expiration_date)
    else:
        expiration_date = note[-1]
        title = ' '.join(note[:-2])
        add(items, title, Decimal(note[-2]), expiration_date)

def find(items, needle):
    list = []
    for item in items:
        if needle.lower() in item.lower():
            list.append(item)
    if len(list) == 0:
        return 'Ничего не найдено'
    else:
        return list

def amount(items, needle):
    for item in items:
        if needle.lower() == item.lower():
            summ = 0
            for product in items[item]:
                summ += product['amount']
            return summ
        else:
            return f'Продукт {needle} не найден'

# Добавляем продукт с названием 'Яйца', количество - 10 шт.
add(goods, 'Яйца', Decimal('10'), '2023-9-30')
add(goods, 'Яйца', Decimal('3'), '2025-12-15')
add(goods, 'Вода', Decimal('2.5'))
add_by_note(goods, 'Яйца гусиные 4 2023-07-15')
add_by_note(goods, 'Хвосты мышиные 5')
print(goods)
print(find(goods, 'йц'))
print(amount(goods, 'яйца'))
print(amount(goods, 'морковь'))