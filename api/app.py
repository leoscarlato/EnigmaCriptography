# save this as app.py
from flask import Flask,request, jsonify
from funcoes import enigma, de_enigma
from matrizes import matriz_permutacao, matriz_auxiliar

app = Flask(__name__)

@app.route("/")
def vizualizacao(methods=['GET']):
    return "Hello, World!"


@app.route('/enigma', methods=['POST'])
def cripto():
    request_data = request.get_json()
    mensagem = request_data['mensagem']
    mensagem_criptografada = enigma(mensagem,matriz_permutacao,matriz_auxiliar)
    return jsonify({"mensagem_criptografada": mensagem_criptografada})


  


@app.route("/deenigma", methods=['POST'])
def descripto():
    request_data = request.get_json()
    mensagem_criptografada = request_data["mensagem_criptografada"]
    mensagem = de_enigma(mensagem_criptografada,matriz_permutacao,matriz_auxiliar)
    return jsonify({"mensagem": mensagem})

if __name__ == '__main__':


    app.run(debug= False)
