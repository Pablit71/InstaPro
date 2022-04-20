from flask import Flask, request, render_template, send_from_directory, Blueprint, jsonify
from utils import get_posts_all, get_post_by_pk
import json

DATA = 'data/data.json'
search_blueprint = Blueprint('search_blueprint', __name__, static_folder='static', template_folder="templates")


@search_blueprint.route('/api/posts/')
def posts_json():
    post = [x for x in get_posts_all()]
    posts = post[0:10]
    return jsonify(posts)


@search_blueprint.route('/api/posts/<int:x>')
def post_json(x):
    post = get_post_by_pk(x)
    return jsonify(post)


if __name__ == "__main__":
    search_blueprint.run()
