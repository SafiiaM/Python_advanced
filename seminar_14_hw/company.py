import json
import os

from create_json import create_employe
from employe import Employe


class LevelException(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return f'{self.msg}'


class Company:

    def __init__(self, name: str):
        self.name = name
        if os.path.exists(f'{self.name}.json'):
            with open(f'{self.name}.json', 'r', encoding='UTF-8') as file:
                employes_list = json.load(file)
        else:
            employes_list = create_employe(name, 10)
        self.employes = [Employe(name_, lvl, id_)
                          for lvl, person in employes_list.items()
                          for id_, name_ in person.items()]

    def log(self, name: str, employe_id: str):
        for item in self.employes:
            if item.name == name and item.employe_id == employe_id:
                return item
        return False

    def get_job(self, employer: Employe, employe_name: str, employe_level: int | str, employe_id: str):
        if employer:
            if employer.lvl_access > int(employe_level):
                if employe_id not in [employe.employe_id for employe in self.employes]:
                    self.employes.append(Employe(employe_name, int(employe_level), employe_id))
                    self.__save()
            else:
                raise LevelException('Ошибка уровня доступа')
        else:
            raise LevelException('Ошибка доступа')

    def __save(self):
        employes_dict = {}
        for employe in self.employes:
            if employe.lvl_access in employes_dict:
                employes_dict[employe.lvl_access][employe.employe_id] = employe.name
            else:
                employees_dict[employe.lvl_access] = {employe.employe_id: employe.name}
        with open(f'{self.name}.json', 'w', encoding='UTF-8') as file:
            json.dump(employes_dict, file, indent=4, ensure_ascii=False)
