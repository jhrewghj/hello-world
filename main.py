import sys
from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
import hashing as h
app = Flask(__name__)
CORS(app)
#put hashing print over here
@app.route('/submit', methods=['POST'])

def submit_data():
    data = request.get_json()
    u_and_p = [data['name'], data['message']]
    c = h.hashedinfo(u_and_p[0], u_and_p[1])
    print("Received data:", data)
    response = {"message": "some data"}
    print(data)
    d = ["a226abda121d6a22bbb9d858a94c9ce1","55be20677b1caac1b4d53058800b06ef"]
    e = ['e2884f8636953a76dc7833ec63f081f3', 'eeaf08b96e493abb74af595db835f36c'] #ilovedogs, 1oi6bm
    f = ['3ed6d0fac7dcd33714fed5c9d3b0076f', '38659adc997e4898eb812b2de57e5297'] #tinf0il, tinfoil

    if c == d:
        return jsonify({"message": "https://dogs"}), 200
    else if c == e:
        return jsonify({"message": "https://dogs"}), 200
    else if c == f:
        return jsonify({"message": "https://tin"}), 200
    else:
        return jsonify({"message": "do normal"}), 200

# This block is for running your Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
