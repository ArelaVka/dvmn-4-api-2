import requests
import json

token='98c56de89e6e0b5b035ffd02f1f4b1da05e72094'

def cut_url(api_token, long_url):
  url_shorten='https://api-ssl.bitly.com/v4/shorten'
  headers_user = {'Authorization': 'Bearer ' + api_token}
  json_url = {'long_url': long_url}
  response_post = requests.post(url_shorten, headers=headers_user, json=json_url)
  return response_post.json().get('link')

url='https://ya.ru/'

print(cut_url(token, url))
