import pickle
from re import sub
import requests
import os

img_url = "http://www.pythonchallenge.com/pc/def/banner.p"
img_content = requests.get(img_url).content
os.makedirs("./assets/5", exist_ok=True)
if not os.path.exists("./assets/5/banner.p"):
    with open("./assets/5/banner.p", "wb") as f:
        f.write(img_content)
result = pickle.load(open("assets/5/banner.p", "rb"))
for item in result:
    for subitem in item:
        for i in range(subitem[1]):
            print(subitem[0], end="")
    print()