import requests
import re

#Obtendo html
nothing = 44827
divide = False
while nothing:
    print(f'----------------------------------------\ncurrent nothing is: {nothing}')
    url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}"
    html = requests.get(url).text
    print(html)
    numbers = re.findall('(?<=nothing is\s)\d+', html)
    if(numbers):
        nothing = numbers[0]
    elif divide == True:
        nothing = numbers[0]
        nothing = int(nothing)/2
    else:
        nothing = int(nothing)/2
        divide = True
