from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    email = request.json.get('email','').lower()
    if 'urgent' in email or 'asap' in email:
        priority = 'High'
    elif 'meeting' in email:
        priority = 'Medium'
    else:
        priority = 'Low'
    return jsonify({'priority': priority})

if __name__ == '__main__':
    app.run(debug=True)
