import pytest
from app import app
import json
from data.data_test import data_test



def test_1():
    response = app.test_client().get('/api/posts/')
    assert type(response.json) == list, 'Это не список'
    assert len(response.json) == 8, 'Ошибка в кол-ве'


def test_2():
    response = app.test_client().get('/api/posts/')
    for k in data_test[0]:
        if k in response.json[0].keys():
            continue
        else:
            assert k in response.json[0].keys(), f'не тот ключ {k} в  посте'

    for k in data_test[1]:
        if k in response.json[1].keys():
            continue
        else:
            assert k in response.json[1].keys(), f'не тот ключ {k} в  посте'

    for k in data_test[2]:
        if k in response.json[2].keys():
            continue
        else:
            assert k in response.json[2].keys(), f'не тот ключ {k} в  посте'

    for k in data_test[3]:
        if k in response.json[3].keys():
            continue
        else:
            assert k in response.json[3].keys(), f'не тот ключ {k} в  посте'

    for k in data_test[4]:
        if k in response.json[4].keys():
            continue
        else:
            assert k in response.json[4].keys(), f'не тот ключ {k} в  посте'

    for k in data_test[5]:
        if k in response.json[5].keys():
            continue
        else:
            assert k in response.json[5].keys(), f'не тот ключ {k} в  посте'

    for k in data_test[6]:
        if k in response.json[6].keys():
            continue
        else:
            assert k in response.json[6].keys(), f'не тот ключ {k} в  посте'

    for k in data_test[7]:
        if k in response.json[7].keys():
            continue
        else:
            assert k in response.json[7].keys(), f'не тот ключ {k} в посте'


def test_3():
    response = app.test_client().get('/api/posts/1')
    assert type(response.json) == dict, 'Это не словарь'
    assert 'content' in response.json.keys(), 'Нет нужного ключа - content'
