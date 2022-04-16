import json

DATA = 'data/data.json'
COMMENTS = 'data/comments.json'


def get_posts_all():
    with open(DATA, 'r', encoding='utf-8') as file:
        posts = json.load(file)
        return posts


def get_comments_all():
    with open(COMMENTS, 'r', encoding='utf-8') as file:
        comments = json.load(file)
        return comments


def get_posts_by_user(user_name):
    post = [x for x in get_posts_all() if user_name in x['poster_name']]
    return post


def get_comments_by_post_id(post_ids):
    comment = [x for x in get_comments_all() if post_ids == x['post_id']]
    return comment


def search_for_posts(query):
    posts = [x for x in get_posts_all() if query in x['content'].lower()]
    return posts


def get_post_by_pk(pk):
    with open(DATA, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for post in data:
            if pk == post['pk']:
                return post


