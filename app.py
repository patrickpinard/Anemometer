from flask import Flask, request, render_template, jsonify
import os, time
from myLOGLib import LogEvent
import random
#from anenometer import Anemometer

app = Flask(__name__)

#ANEMOMETER = Anemometer()

@app.route('/', methods=['GET'])
def index():
        
    #return ('', 204)   
    return render_template('index.html')

@app.route('/windspeed', methods=['POST','GET'])
def windspeed():
    '''
    Retourne la vitesse du vent en m/s
    '''
    if request.method == "GET":
        windspeed = random.randrange(0,35)
        data = {'WINDSPEED': windspeed}
        #windspeed = ANEMOMETER .read()
        return jsonify(data)  
    
    if request.method == "POST":
        return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port = 80, debug=True)