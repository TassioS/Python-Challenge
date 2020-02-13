import requests
import re
#Obtendo html
url = "http://www.pythonchallenge.com/pc/def/equality.html"
html = requests.get(url).text

#Separando caracteres relevantes:
string = html.split("kAewtlo")[1][0:-4]

#Pegando todos os caracteres que seguem o padrão XXXXzXXXXX
string = re.findall("[A-Z]{3,10}[a-z]{1}[A-Z]{3,10}",string)
aux = []

#Filtrando os caracteres para o padrão que tenha exatamente 3 maiusculas/uma minuscula/ três maiusculas XXXzXXX
for x in string:
    if x[0].isupper() and x[1].isupper() and x[2].isupper() and not x[3].isupper() and x[4].isupper() and x[5].isupper() and x[6].isupper() and len(x) == 7:
        aux.append(x)

#Montando uma string com apenas as letras minusculas das strings restantes:
resultado = ""
for item in aux:
    for letra in item:
        if not letra.isupper():
            resultado += letra
print(resultado)