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
    users = [
        {"id": 1, "name": "Thaam T."},
        {"id": 2, "name": "Shermin M."},
        {"id": 3, "name": "Alex P."},
        {"id": 4, "name": "Linda S."}
    ]
    return jsonify(users)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
