from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def data():
    return jsonify({'message': 'Hola desde Python!'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
