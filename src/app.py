from flask import Flask, jsonify, request
app = Flask(__name__)



@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos),200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print(todos.append)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    print("This is the position to delete:", position)
    return jsonify(todos), 200


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)