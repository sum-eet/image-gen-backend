import requests
import json
from datetime import date

from PIL import Image, ImageDraw, ImageFont

api_key = "7638b275fa48d444307195f574fdb28e"
city = "Pune"
# url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=7638b275fa48d444307195f574fdb28e&units=metric".format(
#     city)

# response = requests.get(url)
# data = json.loads(response.text)
# print(data)

image = Image.open("post.png")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Inter.ttf', size=50)
content = "Latest Weather Forecast"


color = 'rgb(255,255,255)'
draw.text((55, 50), content, color, font=font)

image.show("testtoday22.png")
