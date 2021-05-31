import requests

print("Script para buscar información")
datosEncontrados = requests.get(" http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json")

print ("--------------------------------------------------------------")
print(datosEncontrados.content)
print(type(datosEncontrados))
print ("--------------------------------------------------------------")

print("Fin Script......")
