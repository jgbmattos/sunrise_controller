from flask import Flask
from flask_restful import Api

from src.utils.url import config_resources

app = Flask(__name__)
api = Api(app)

config_resources(api)


if __name__ == "__main__":
    app.run()