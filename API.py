from flask import Flask, jsonify, request 
from flask_cors import CORS 
from datetime import datetime 

app=Flask(__name__)
CORS(app)

tipo_medicion = {'sensor':'HC-SR04','variable':'distancia','unidades':'cm'}

mediciones = [

]

@app.route('/')
def get():
    return tipo_medicion 


@app.route('/mediciones', methods=['GET'])
def getAll():
    return jsonify(mediciones) 

@app.route('/mediciones', methods=['POST'])
def postOne():
    body = request.json 
    now = datetime.now()
    body['fecha'] = datetime.strftime(now,'%Y-%m-%d %H:%M:%S')
    mediciones.append({**body, **tipo_medicion})
    print("Los valores de la distancia deben estar entre 2cm y 400cm")
    return jsonify(mediciones)

@app.route('/mediciones/getMedia', methods=['GET'])
def getMedia():
    datos = []
    media=0
    j=0
    for i in mediciones:
        datos.append(i['valor'])
    while j<len(datos):
        media=media + datos[j]
        j+=1
    media=media/len(datos)
    x = str(media) 
    return jsonify(valor = x )
   

app.run(port=5000,debug=True)