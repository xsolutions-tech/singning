import os

from flask import Flask, request
from flask.json import jsonify
import json
import base64
import hashlib
import subprocess

app = Flask(_name_)


@app.route('/SigningService', methods=['POST'])
def Sigining():
    if request.method == 'POST':
        #         Serialize=request.form
        ToSerialize = request.data
        js=ToSerialize.decode("utf-8")
        f = open("SourceDocumentJson.json", "w", encoding='utf-8')
        f.write(js)
        f.close()
        ff = open("FullSignedDocument.json", "w", encoding='utf-8')
        ff.write(js)
        print(js)
        ff.close()
        subprocess.run('SubmitInvoices.bat',capture_output=True)
        f = open("FullSignedDocument.json", "r", encoding='utf-8')
        FullSignedDocument = f.read()
        print(FullSignedDocument)
        open("FullSignedDocument.json", "w")
        # return FullSignedDocument
        # print(json.loads(FullSignedDocument)['documents'][0]['signatures'])
        # return json.dumps(json.loads(FullSignedDocument))
        return json.dumps(FullSignedDocument)


if _name_ == '_main_':
    app.run("0.0.0.0", "5050")
