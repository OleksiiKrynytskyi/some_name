from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
CORS(app)
run_with_ngrok(app)

ovocie = ["jablko","pomaranc"]

@app.route("/", methods = ["GET"])
def main():
  slovnik = {"ovocie":ovocie}
  return jsonify(slovnik),200

@app.route("/vytvorit", methods = ["POST"])
def create():
  data = request.get_json(force=True)
  data_dict = dict(data)
  ovocie.append(data_dict["vytvorit"])
  return jsonify("created"),201

@app.route("/upravit/<id>", methods = ["PUT"])
def update(id):
  data = request.get_json(force=True)
  data_dict = dict(data)
  ovocie[int(id)]= data_dict["upravit"]
  return jsonify(updated),201

@app.route("/delete/<id>", methods = ["DELETE"])
def delete(id):
  ovocie[int(id)]= None
  return jsonify(updated),204

app.run()
