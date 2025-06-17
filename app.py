from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["proyecto"]  # Base de datos correcta
collection = db["alumnos"]  # Colección correcta

@app.route("/alumnos")
def get_alumnos():
    data = list(collection.find({}, {"_id": 0}))  # Excluye "_id" para evitar errores con ObjectId
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
