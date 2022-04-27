from app import app
from data_t import get_posts_all


def test_1():
    response = app.test_client().get('/api/posts/')
    assert type(response.json) == list, 'Это не список'


def test_2():
    response = app.test_client().get('/api/posts/')
    all_keys = ['content', 'poster_name', 'pic', 'views_count', 'poster_avatar', 'likes_count', 'pk']
    for post in response.json:
        for key in post.keys():
            assert key in all_keys, f'неверный ключ - {key}'


def test_3():
    for i in range(1, len(get_posts_all())):
        response = app.test_client().get(f'/api/posts/{i}')
        assert type(response.json) == dict, 'Это не словарь'


def test_4():
    for i in range(1, len(get_posts_all())):
        response = app.test_client().get(f'/api/posts/{i}')
        all_keys = ['content', 'poster_name', 'pic', 'views_count', 'poster_avatar', 'likes_count', 'pk']
        for post in response.json:
            assert post in all_keys, f'неверный ключ - {post}'
