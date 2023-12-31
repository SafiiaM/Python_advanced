# Задание №8 Погружение в Python | Коллекции
# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей

baggage = {
    'Денис': ('кружка', 'ложка', 'еда'),
    'Саня': ('палатка', 'фонарь', 'гитара'),
    'Антоха': ('посуда', 'еда', 'горелка')
}

all_items = set(baggage['Денис'])&set(baggage['Саня'])&set(baggage['Антоха'])
uniq_items = set(baggage['Денис'])^set(baggage['Саня'])^set(baggage['Антоха'])
common_items_except_one = (
      set(baggage['Денис'])|
      set(baggage['Саня'])|
      set(baggage['Антоха'])
)-    set(baggage['Денис']), (
      set(baggage['Денис'])|
      set(baggage['Саня'])|
      set(baggage['Антоха'])
) -   set(baggage['Саня']), (
        set(baggage['Денис'])|
        set(baggage['Саня'])|
        set(baggage['Антоха'])
) - set(baggage['Антоха'])

names = ['Денис','Саня','Антоха']
missing_items = {}

for item_set, names in zip(common_items_except_one, names):
    for item in item_set:
        missing_items[item] = names

print(f'Вещи взяли все три друга: ', baggage)
print(f'Вещи уникальны, есть только у одного друга: ', uniq_items)
print(f'Вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует: ', missing_items)
