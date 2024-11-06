"""Exemplo de aplicação RESTful com Flask - Arquivo principal."""

from flask import Flask
from flask_restful import Api
from resources.todo import Todo, TodoList

app = Flask(__name__)
api = Api(app)


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run()