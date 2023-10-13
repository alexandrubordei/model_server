from flask import Flask, request, jsonify
import logging
import json

from _model import *

from urllib.parse import urlparse,unquote

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)

logging.info("Ready to serve models")

@app.route('/infer', methods=['PUT','POST'])
def infer():
    rq = json.loads(request.data)

    if 'prompt' not in rq:
        return "invalid request: missing prompt param", 400
    
    temperature=0.2

    if 'temperature'  in rq:
        temperature=rq['temperature']

    prompt=rq['prompt']
    logging.info(f"working on: {prompt}")

    resp=generate_text(prompt, temperature)

    return jsonify({"response":resp}), 200
