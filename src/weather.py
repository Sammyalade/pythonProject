import requests

url = "https://avatars.githubusercontent.com/u/151362938?s=400&u=f83a46b7dbbba3f8c48862e035bf7d7bda9bdcb5&v=4"
r = requests.get(url)

with open('femi.png', mode='wb') as mf:
    mf.write(r.content)


#url = 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'

#r = requests.get(url)
#print(r.json())
