from flask import Flask, abort, jsonify, request
from flask_restful import Resource, Api,reqparse

app = Flask(__name__)
api = Api(app)

todos = {
    1: {"task" : "Write Hello wold program", "summary" : "Write a code by using python"},
    2: {"task" : "Write Palindrome program", "summary" : "Write a code by using python"},
    3: {"task" : "Write Calculator program", "summary" : "Write a code by using python"}
}

demo_post = reqparse.RequestParser()
demo_post.add_argument('task', type=str, help='Task is required', required=True)
demo_post.add_argument('Summary', type=str, help='Summary is required', required=True)

demo_put = reqparse.RequestParser()
demo_put.add_argument('task', type=str),
demo_put.add_argument('summary', type=str)


class ToDoList(Resource):
    def get(self):
        return todos
    
class ToDo(Resource):
    def get(self, todo_id):
        return todos[todo_id]

    def post(self, todo_id):
        pars = demo_post.parse_args()
        if todo_id in todos:
            abort(409, 'task is already taken')
        todos[todo_id] = {'task' : pars["task"], 'Summary' : pars["Summary"]}
        return todos[todo_id]

    def put(self, todo_id):
        pars = demo_put.parse_args()
        if todo_id in todos:
            abort(404, "task doesn't exist, cannot update")
        if pars['task']:
            todos[todo_id]['task'] = pars['task']
        if pars['summary']:
            todos[todo_id]['summary'] = pars['summary']
        return todos[todo_id]

    def delete(self, todo_id):
        del todos[todo_id]
        return todos

    
api.add_resource(ToDoList, '/todos')
api.add_resource(ToDo, '/todos/<int:todo_id>')


if __name__=="__main__":
    app.run(debug=True)