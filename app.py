from concurrent.futures import thread
from flask import Flask, jsonify, request

app = Flask(__name__)

# ! WARNING !!
# ? what happens if we change ...
# * this is an important


class TodoList():
    def __init__(self) -> None:
        self.todo_list = [
            {
                "Title": "Finish To do List",
                "Due": "july 30"
            },
            {
                "Title": "Answer question",
                "Due": "july 30"
            },
            {
                "Title": "another task",
                "Due": "Aug 5"
            }
        ]

    def add_todo(self, item):
        """Add a new todo list item

        Args:
            item (dict): this is the item list
        """
        self.todo_list += [item]

    def get_todos(self):
        return self.todo_list


todolist = TodoList()
todolist.add_todo()


@app.route("/")
def home():
    return "<h1>This is Home</h1>"


@app.route("/todolist", methods=["GET"])
def get_t():
    return jsonify(todolist.get_todos())


@app.route("/todolist/add", methods=["POST"])
def add_item():
    data = request.json
    todolist.add_todo(data)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
