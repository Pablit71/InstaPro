from flask import Flask, request, render_template, send_from_directory
from main.main import main_blueprint
from detail.detail import search_blueprint
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)

if __name__ == "__main__":
    app.run()
