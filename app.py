import flask
from flask_restful import Resource, Api

app = flask.Flask(__name__)
api = Api(app)

# Class

# api.add_resource(ClassName, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)