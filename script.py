import requests
import json

token='98c56de89e6e0b5b035ffd02f1f4b1da05e72094'

def cut_url(api_token, long_url):
  url_shorten='https://api-ssl.bitly.com/v4/shorten'
  headers_user = {'Authorization': 'Bearer ' + api_token}
  json_url = {'long_url': long_url}
  response_post = requests.post(url_shorten, headers=headers_user, json=json_url)
  return response_post.json().get('id')

def count_clicks(bitlink):
  url_total='https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(bitlink)
  payload={"unit":"day", "units": "-1"}
  responce=requests.get(url_total, params=payload)
  print(responce.url)
  print(responce.text)

#url=input()
url='http://ya.ru'
bitlink=cut_url(token, url)
if bitlink:
  count_clicks(bitlink)
else:
  print('Your url is incorrect!')
