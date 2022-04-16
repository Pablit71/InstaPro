from flask import Flask, request, render_template, send_from_directory, Blueprint
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, get_comments_all, get_posts_by_user

main_blueprint = Blueprint('main', __name__, static_folder='static', template_folder="templates")


@main_blueprint.route('/')
def main():
    posts = [x for x in get_posts_all()]
    return render_template('index.html', posts=posts)


@main_blueprint.route('/post/<int:x>')
def posts(x):
    posts = get_post_by_pk(x)
    comments = get_comments_by_post_id(x)
    amount_com = len(comments)
    return render_template('post.html', posts=posts, comments=comments, amount_com=amount_com)


@main_blueprint.route('/post/search/')
def search():
    search_by = request.args['s']
    posts = [x for x in get_posts_all() if search_by in x['content'].lower()]
    amount_post = len(posts)
    return render_template('search.html', posts=posts, amount_post=amount_post)


@main_blueprint.route('/users/<username>')
def user_name(username):
    user = get_posts_by_user(username)
    return render_template('user-feed.html', user=user)
