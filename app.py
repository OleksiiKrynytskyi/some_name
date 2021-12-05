from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
CORS(app)
run_with_ngrok(app)

ovocie = ["jablko","pomaranc","jahoda"]

@app.route("/", methods = ["GET"])
def main():
  myDb = MYSQL.connect(host = "147.232.40.14", user = "ok529nk", passwd = "Aiphu60C", database = "ok529nk")
  cursor = myDb.cursor()
  cursor.execute("SELECT Nazov from Ovocie")
  result = cursor.fetchall()
  cursor.close()
  vysledok = []
  for i in result:
    vysledok.append('{'+'{}'.format(i[0])+'}')
  vys = []
  for i in range(len(vysledok)):
    vys.append(eval(vysledok[k]))
  myDb.close()
  slovnik = {"ovocie":vys}
  return jsonify(slovnik),200


@app.route("/upravit/<id>", methods = ["PUT"])
def update(id):
  data = request.get_json(force=True)
  data_dict = dict(data)
  ovocie[int(id)]= data_dict["upravit"]
  return jsonify("updated"),201

@app.route("/vymazat/<id>", methods = ["DELETE"])
def delete(id):
  del ovocie[int(id)]
  return jsonify("deleted"),204

app.run()
