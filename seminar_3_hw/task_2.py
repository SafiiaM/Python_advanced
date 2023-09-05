# ✔ В большой текстовой строке подсчитать количество встречаемых
# # слов и вернуть 10 самых частых. Не учитывать знаки препинания
# # и регистр символов. За основу возьмите любую статью
# # из википедии или из документации к языку

text = input("Введите текст: ").lower() \
    .replace(',', '').replace('.', '').replace('!', '').replace('?', '').split(' ')
my_dict = dict()
for item in text:
    if item not in my_dict.keys():
        my_dict[item] = 1
    else:
        my_dict[item] += 1
my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
l = 10
if len(my_dict) <= 10:
    l = len(my_dict)
print(my_dict)
for i in range(l):
    print(list(my_dict)[i], end=' ')

    # https://ru.wikipedia.org/wiki/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_%D0%B8_%D0%A0%D0%BE%D0%B3%D0%BD%D0%B5%D0%B4%D0%B0
    # статья для проверки