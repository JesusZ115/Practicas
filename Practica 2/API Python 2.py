import requests

print("Script para buscar información")
datosEncontrados = requests.get(" https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP74665,SF61745,SF60634,SF43773/datos/oportuno?token=9dd76aba613e11ae6bf8819c50a4cb663e5d82262598e8f223ecd2706a06071c")

print ("--------------------------------------------------------------")
print(datosEncontrados.content)
print(type(datosEncontrados))
print ("--------------------------------------------------------------")

print("Fin Script......")
