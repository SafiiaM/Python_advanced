import random
import json
from faker import Faker


def create_employe(company: str, count: int):
    employes = {}
    list_id = []
    for _ in range(count):
        while True:
            name = Faker('ru_RU').name()
            if len(name.split()) == 3:
                break
        while True:
            employe_id = str(random.randint(1, 999999)).zfill(6)
            if employe_id not in list_id:
                list_id.append(employe_id)
                break
        lvl_access = int(employe_id) % 7 + 1
        if lvl_access in employes:
            employes[lvl_access][employe_id] = name
        else:
            employes[lvl_access] = {employe_id: name}

    with open(f'{company}.json', 'w', encoding='UTF-8') as file:
        json.dump(employes, file, indent=4, ensure_ascii=False)
    return employes