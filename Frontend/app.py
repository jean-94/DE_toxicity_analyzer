from flask import Flask, request, send_file, jsonify, render_template
import requests

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('site.html')

@app.route('/get/speech', methods=['POST'])
def get_sentence():
    speech = request.get_json()['speech']
    statistics = requests.get(f'http://model:5000/toxic?values={speech}')
    return jsonify(statistics.text)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
