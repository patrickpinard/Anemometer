# Auteur  : Patrick Pinard 
# Date    : 8.1.2022
# Objet   : anémomètre 
# Version : 1.0

# -*- coding: utf-8 -*-

#   Clavier MAC :      
#  {} = "alt/option" + "(" ou ")"
#  [] = "alt/option" + "5" ou "6"
#   ~  = "alt/option" + n    
#   \  = Alt + Maj + / 

 
# Vitesse du vent : 0 ~ 32.4 m / s
# Alimentation anémomètre: 12 V  (7V ~ 24 V DC)
# Tension de sortie: 0,4 ~ 2V 
# 0.4V (0 m/s wind) up to 2.0V (for 32.4m/s wind speed).
# Anemometer      name     4 pin ADC
# blue (signal)   A0       jaune
# brown (+12)	  Vin      rouge
# black (Gnd)	  Gnd      noir

from adc    import ADC
from time   import sleep
import re

# Valeurs min et max en Volts de l'anémomètre et conversion en m/s
anemometer_min_volts = 0
anemometer_max_volts = 2.8
min_wind_speed = 0.0
max_wind_speed = 32.4

def mapRange(value, inMin, inMax, outMin, outMax):
    return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))

def truncate(num):
    '''
    truncate number to 2 digits but return a string
    '''
    return re.sub(r'^(\d+\.\d{,2})\d*$',r'\1',str(num))

class Anemometer(object):

    """
    Classe definissant un anénomètre caracterisés par les méthodes : 
        - read : retourne la vitesse du vent en m/s  
        
    """

    def __init__(self):
        """
        Constructeur de la classe  : 

        - name  : nom de la sonde 
        - id : identifiant de la sonde 
        - unit : l'unité de mesure 
        - type : type de sonde (
        - unit : unité de valeur mesurée
        - adc_channel : n+ du canal sur ADC
        - windspeed : retourne la mesure en m/s
        """

        self.id = 1
        self.adc = ADC()
        self.adc_channel = 4
        self.name = "sonde de vitesse du vent"                                                    
        self.type = "" 
        self.unit = 'm/s'
        
    def __repr__(self):

        """
        Méthode permettant d'afficher les paramètres principaux d'une sonde de température.
        """

        return "\nSensor Information : \n name   : {}\n type   : {}\n   id   : {}\n unit   : {} ".format(self.name, self.type, self.id, self.unit)

    def read(self):

        """
        Méthode retournant la vitesse du vent en m/s.
        """
        
        anemometer_voltage = ADC.read_voltage(self.adc, self.adc_channel)/1000
        if anemometer_voltage > 0.4:
            windspeed = (anemometer_voltage -0.4) / 2.0 * 32.4
        else:
            windspeed = 0.00
        print('Windspeed [km/h] : ' ,'{:3.2f}'.format(windspeed),  end = "\r")
        return  round(windspeed,2) 
        
   
if __name__ == "__main__":

    print(" ---- test Anémomètre  -----")
    WindSpeedSensor = Anemometer()
    while True:
        volts, windspeed  = WindSpeedSensor.read()
        print('Windspeed [km/h] : ' ,'{:3.2f}'.format(windspeed),  end = "\r")
        sleep(0.5)

   






