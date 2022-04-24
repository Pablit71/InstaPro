import pytest
from app import app
import json


def test():
    response = app.test_client().get('/api/posts/')
    assert type(response.json) == list, 'Это не список'
    assert len(response.json) == 8, 'Ошибка в кол-ве'
    assert response.json[0]['poster_name'] == 'leo', 'не то имя'


def test_2():
    response = app.test_client().get('/api/posts/1')
    assert type(response.json) == dict, 'Это не словарь'
    assert 'content' in response.json.keys(), 'Нет нужного ключа - content'
