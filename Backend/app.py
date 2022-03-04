from flask import Flask, request
from detoxify import Detoxify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'status code = 200'

@app.route('/mean', methods = ['GET'])
def mean():
    values_str = request.args.get('values', type=str)
    if values_str is Empty:
        return 'Error'
    else :
        return str(Detoxify(checkpoint = "toxic_original-c1212f89.ckpt",device="cpu").predict(values_str))
       
