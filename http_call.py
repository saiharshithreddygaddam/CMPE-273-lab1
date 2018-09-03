import requests

# get the url request
r = requests.get('https://webhook.site/a3f70ce9-99a8-434f-a4fe-3ef1a24d350f')
# output the date 
print(r.headers['Date'])
