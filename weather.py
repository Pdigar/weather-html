# -*- coding: utf-8 -*-
import requests
import json

ciudades = {"1":"Almería","2":"Cádiz","3":"Córdoba","4":"Granada","5":"Huelva","6":"Jaén","7":"Málaga","8":"Sevilla","9":"Dos Hermanas"}

print """
1. Almería
2. Cádiz
3. Córdoba
4. Granada
5. Huelva
6. Jaén
7. Málaga
8. Sevilla
9. Dos Hermanas
"""

eleccion = raw_input("Elige una de estas ciudades andaluzas y te dare su temperatura actual: ")

respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % ciudades[eleccion]})
diccionario = json.loads(respuesta.text)

tempkelvin = diccionario["main"]["temp"]

tempreal = round(tempkelvin - 273.15 ,1)

print "La temperatura actual de %s es %s grados centígrados" % (ciudades[eleccion],tempreal)
