import pytest
from app import search_blueprint
import json


def test():
    response = search_blueprint.get('/api/posts/')
    assert response == [], 'Это не список'
