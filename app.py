from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/processar-indicacao", methods=["POST"])
def processar_indicacao():
    try:
        data = request.form
        nome = data.get("nome")
        email = data.get("email")
        telefone = data.get("telefone")
        nome_indicado = data.get("nome_indicado")
        email_indicado = data.get("email_indicado")
        empresa_indicada = data.get("empresa_indicada")
        telefone_indicado = data.get("telefone_indicado")

        # Simulação de processamento
        print(f"Nome: {nome}, Email: {email}, Nome indicado: {nome_indicado}")

        return jsonify({"message": "Indicação enviada com sucesso!"}), 200
    except Exception as e:
        print("Erro ao processar a indicação:", e)
        return jsonify({"error": "Erro ao processar sua solicitação."}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=80)
