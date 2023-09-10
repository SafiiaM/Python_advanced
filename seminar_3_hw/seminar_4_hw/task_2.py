# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def reverse_key(**kwargs):
    temp = {}
    for key, value in kwargs.items():
        if not isinstance(value, str):
            value = str(value)
        temp[value] = key
    return temp


print(reverse_key(std=[100, 300, -500], skb=[150, 600, -700], srd=[400, 400, -400]))

# {'[100, 300, -500]': 'std', '[150, 600, -700]': 'skb', '[400, 400, -400]': 'srd'}

# решение преподавателя:

def inverse_try(**kwargs) -> dict:
    new_dict={}
    for key,value in kwargs.items():
       try:
           new_dict[value]=key
       except:
           new_dict[str(value)]=key
    return new_dict

def inverse_instance(**kwargs) -> dict:
    new_dict={}
    for key,value in kwargs.items():
       if not isinstance(value, list|set|dict):
           new_dict[value]=key
       else:
           new_dict[str(value)]=key
    return new_dict
print(inverse_try(one=1, two=['2'], three=(3,)))
print(inverse_instance(one=1, two=['2'], three=(3,)))

# {1: 'one', "['2']": 'two', (3,): 'three'}
# {1: 'one', "['2']": 'two', (3,): 'three'}