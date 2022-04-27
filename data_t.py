import json

DATA = 'data/data.json'


def get_posts_all():
    with open(DATA, 'r', encoding='utf-8') as file:
        posts = json.load(file)
        return posts
