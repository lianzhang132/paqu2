import requests
import os


headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
    }

url = "https://tudou.com-l-tudou.com/share/6cb993c8fa82ad11ff71fad64d213a72"

response = requests.get(url=url, headers=headers)
img = response.content
print(img)
with open("2.mp4", 'wb') as f:
    f.write(img)