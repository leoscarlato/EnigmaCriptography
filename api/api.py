# save this as app.py
from flask import Flask,request, jsonify
from enigmamachine import enigma_machine, enigma_machine_decrypt
from matrices import permute_matrix, auxiliary_matrix

app = Flask(__name__)


@app.route('/enigma/encrypt', methods=['POST'])
def encrypt():
    request_data = request.get_json()
    text = request_data['text']
    encrypt_text = enigma_machine(text,permute_matrix,auxiliary_matrix)
    return jsonify({"encrypt_text": encrypt_text})


@app.route("/enigma/decrypt", methods=['POST'])
def decrypt():
    request_data = request.get_json()
    encrypt_text = request_data["encrypt_text"]
    text = enigma_machine_decrypt(encrypt_text,permute_matrix,auxiliary_matrix)
    return jsonify({"text": text})

if __name__ == '__main__':
    app.run(debug= False)
