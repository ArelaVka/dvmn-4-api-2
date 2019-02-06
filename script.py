import requests
import json

token='98c56de89e6e0b5b035ffd02f1f4b1da05e72094'

def cut_url(api_token, long_url):
  url_shorten='https://api-ssl.bitly.com/v4/shorten'
  headers_user = {'Authorization': 'Bearer ' + api_token}
  json_url = {'long_url': long_url}
  response_post = requests.post(url_shorten, headers=headers_user, json=json_url)
  return response_post.json().get('id')

def count_clicks(api_token, bitlink):
  url_total='https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(bitlink)
  payload={"unit":"day"}
  headers_user = {'Authorization': 'Bearer ' + api_token}
  responce=requests.get(url_total, headers=headers_user, params=payload)
  return responce.json()["total_clicks"]

#url=input()
url='http://ya.ru'
bitlink=cut_url(token, url)
if bitlink:
  count_clicks(token, bitlink)
else:
  print('Your url is incorrect!')
