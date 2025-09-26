from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)
USERS_FILE = os.path.join(os.path.dirname(__file__), "..", "users.json")


def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            f.write("[]")
    with open(USERS_FILE, "r") as file:
        return json.load(file)

def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    users = load_users()

    if any(user["email"] == data["email"] for user in users):
        return jsonify({"message": "Email déjà utilisé."})

    users.append({
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "email": data["email"],
        "password": data["password"]
    })
    save_users(users)
    return jsonify({"message": "Compte créé avec succès !"})

@app.route("/api/login", methods=["POST"])
def login_user():
    data = request.get_json()
    users = load_users()
    user = next((us for us in users if us["email"] == data["email"] and us["password"] == data["password"]), None)
    if user:
        return jsonify({"message": f"Connecté : {user['first_name']} {user['last_name']}"})
    else:
        return jsonify({"message": "Email ou mot de passe incorrect"})


if __name__ == "__main__":
    app.run(debug=True)
