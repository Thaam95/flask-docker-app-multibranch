from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask API!"})

@app.route('/api/goodbye', methods=['GET'])
def goodbye():
    return jsonify({"message": "Goodbye from Flask API!"})

@app.route('/api/users', methods=['GET'])
def users():
    users_list = [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
        {"id": 3, "name": "Bob Johnson", "email": "bob@example.com"},
        {"id": 4, "name": "Alice Williams", "email": "alice@example.com"},
        {"id": 5, "name": "Charlie Brown", "email": "charlie@example.com"},
        {"id": 6, "name": "Eve Davis", "email": "eve@example.com"},
        {"id": 7, "name": "Frank Miller", "email": "frank@example.com"}
    ]
    return jsonify(users_list)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
