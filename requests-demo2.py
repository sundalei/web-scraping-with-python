import requests

r = requests.get('https://api.github.com/user', auth=('sundalei', 'sundalei1988'))
result = r.text
print(result)