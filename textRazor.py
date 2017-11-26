import requests, json

api_key= "ee8df0e3a42d45d65c21ed41c6b1975f913d7050dfc40c5301826758"
headers = {
    'x-textrazor-key': api_key,
}

data = [
  ('extractors', 'entities,entailments'),
  ('text', "Hello, we are the thunder panthers."),
]


resp = requests.get("https://api.textrazor.com/", headers = headers, data = data)
ret = resp.json()
print ret['response']['entailments']

