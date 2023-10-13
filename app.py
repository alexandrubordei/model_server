from flask import Flask, request, jsonify
import logging
import json

from model import *

from urllib.parse import urlparse,unquote

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)

@app.route('/infer', methods=['PUT','POST'])
def infer():
    rq = json.loads(request.data)
    if 'prompt' not in rq:
        return "invalid request: missing prompt param", 400

    prompt=rq['prompt']  
    logging.info(f"working on: {prompt}")

    resp=model.generate_text(prompt)

    return jsonify({"response":resp}), 200
