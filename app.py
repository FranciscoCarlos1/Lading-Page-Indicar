# Backend (Python - Flask)

from pickle import APPEND
from flask import jsonify, request
from flask_cors import CORS
import flask_cors
CORS(APPEND) , request, jsonify

app = flask_cors(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        # Here you can handle the data, e.g., save to a database or send an email
        print(f"Name: {name}, Email: {email}, Message: {message}")

        return jsonify({"message": "Formulário enviado com sucesso!"}), 200
    except Exception as e:
        print("Erro ao processar o formulário:", e)
        return jsonify({"error": "Houve um problema ao processar sua solicitação."}), 500

if __name__ == "__main__":
    app.run(debug=True)
