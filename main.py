# usrnme:hi,psswd:abc123



from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Allow requests from all origins (replace with specific origins for production)
CORS(app)

# This is where you define your routes
@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    print("Received data:", data)
    response = {"message": "some data"}
    print(data)
    if data == {'name': 'username=hi', 'message': '1'}:
        return jsonify({"message": "https://tinf0il.tech"}), 200
    else:
        return jsonify({"message": "do normal"}), 200

# This block is for running your Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
