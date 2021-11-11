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
        f = open("SourceDocumentJson.json", "w")
        f.write(js)
        f.close()
        subprocess.run('SubmitInvoices.bat',capture_output=True)
        f = open("FullSignedDocument.json", "r")
        FullSignedDocument = f.read()
        return FullSignedDocument


if _name_ == '_main_':
    app.run("0.0.0.0", "5050")
