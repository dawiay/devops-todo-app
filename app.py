from flask import Flask, jsonify, request

app = Flask(__name__)
todos = []

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    todos.append(data.get("task"))
    return jsonify(todos), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
