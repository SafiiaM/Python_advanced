import os

import pytest

from company import Company, LevelException
from employe import Employe


@pytest.fixture
def name():
    name = ['Иван Иванович Иванов', '123 Иванов', 'Иван иванович Иванов', 1234]
    return name


@pytest.fixture()
def level():
    level = [1, 8, '-3']
    return level


@pytest.fixture()
def id_():
    id_ = ['000123', '012', 'bd1405']
    return id_


def test_name_type(name, level, id_):
    with pytest.raises(TypeError, match=r'ФИО должно состоять только '
                                        r'из букв и начинаться с большой буквы'):
        Employe(name[3], level[0], id_[0])


def test_name_title(name, level, id_):
    with pytest.raises(ValueError, match=r'ФИО должно состоять только '
                                         r'из букв и начинаться с большой буквы'):
        Employe(name[2], level[0], id_[0])


def test_name_number(name, level, id_):
    with pytest.raises(ValueError, match=r'ФИО должно состоять только '
                                         r'из букв и начинаться с большой буквы'):
        Employe(name[1], level[0], id_[0])


def test_level_1(name, level, id_):
    with pytest.raises(ValueError, match=r'Значение должно быть целым числом от 1 до 7'):
        Employe(name[0], level[1], id_[0])


def test_level_2(name, level, id_):
    with pytest.raises(ValueError, match=r'Значение должно быть целым числом от 1 до 7'):
        Employe(name[0], level[2], id_[0])


def test_id_1(name, level, id_):
    with pytest.raises(ValueError, match=r'ID должен состоять из 6 цифр'):
        Employe(name[0], level[0], id_[1])


def test_id_2(name, level, id_):
    with pytest.raises(ValueError, match=r'ID должен состоять из 6 цифр'):
        Employe(name[0], level[0], id_[2])


def test_eq_1(name, level, id_):
    employe_1 = Employe(name[0], level[0], id_[0])
    employe_2 = Employe(name[0], level[0], id_[0])
    assert employe_1 == employe_2


def test_eq_2(name, level, id_):
    employe = Employe(name[0], level[0], id_[0])
    with pytest.raises(ValueError, match=r'Операция недопустима'):
        employe.__eq__(45)


@pytest.fixture
def set_company(request):
    company = Company('test')

    def teardown():
        if os.path.exists('test.json'):
            os.remove('test.json')

    request.addfinalizer(teardown)

    return company


def test_level_access_1(set_company):
    employe = Employe('Петр Печенкин', 1, '123124')
    name = 'Иван Иванов'
    new_id = '123456'
    lvl = 3
    with pytest.raises(LevelException, match=r'Ошибка уровня доступа'):
        set_company.get_job(employe, name, lvl, new_id)


def test_level_access_2(set_company):
    name = 'Иван Иванов'
    new_id = '123456'
    lvl = 3
    employe = set_company.log(name, new_id)
    with pytest.raises(LevelException, match=r'Ошибка доступа'):
        set_company.get_job(employe, name, lvl, new_id)


if __name__ == '__main__':
    pytest.main(['-v'])