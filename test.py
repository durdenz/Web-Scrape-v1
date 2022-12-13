import requests

url = 'https://codedamn.com'

res = requests.get(url)

txt = res.text
status = res.status_code

print(txt, status)