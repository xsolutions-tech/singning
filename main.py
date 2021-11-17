import os

from flask import Flask, request
from flask.json import jsonify
import json
import base64
import hashlib
import subprocess

app = Flask(__name__)


@app.route('/SigningService', methods=['POST'])
def Sigining():
    if request.method == 'POST':
        ToSerialize = request.data
        js=ToSerialize.decode("utf-8")
        f = open("SourceDocumentJson.json", "w")
        f.write(js)
        f.close()
        ff = open("FullSignedDocument.json", "w")
        ff.write(js)
        ff.close()
        subprocess.run('SubmitInvoices.bat',capture_output=True)
        f = open("FullSignedDocument.json", "r")
        FullSignedDocument = f.read()
        print(FullSignedDocument)
        open("FullSignedDocument.json", "w")
        # return FullSignedDocument
        # print(json.loads(FullSignedDocument)['documents'][0]['signatures'])
        # return json.dumps(json.loads(FullSignedDocument))
        return json.dumps(FullSignedDocument)


if __name__ == '__main__':
    app.run("0.0.0.0", "5050")
