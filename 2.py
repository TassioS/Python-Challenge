import requests
#Obtendo o html da pagina
url = "http://www.pythonchallenge.com/pc/def/ocr.html"
htmlString = requests.get(url).text

#Usando uma parte inicial da cadeia de caracteres para separa-los do restante do html.
mess = htmlString.split('_$^__')[1]

letrasNum = ""
#Eliminando todos os caracteres que não são alfanuméricos
for x in mess:
    if x.isalnum():
        letrasNum += x
#Printando o resultado:
print(letrasNum)