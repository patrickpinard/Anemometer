from flask import Flask, request, render_template, jsonify
import os, time
from myLOGLib import LogEvent
import random
from flask_cors import CORS
from anemometer import Anemometer

app = Flask(__name__)
CORS(app)
ANEMOMETER = Anemometer()

@app.route('/', methods=['GET'])
def index(): 
    return render_template('index.html')

@app.route('/windspeed', methods=['POST','GET'])
def windspeed():
    '''
    Retourne la vitesse du vent en km/h
    '''
    if request.method == "GET":
        #windspeed = random.randrange(0,35)
        windspeed = ANEMOMETER .read() * 3.6 # 1 m/s = 3.6 km/h
        data = {'WINDSPEED': windspeed}
        return jsonify(data)  
    
    if request.method == "POST":
        return render_template('index.html')
        #return ('', 204)  


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port = 80, debug=True)