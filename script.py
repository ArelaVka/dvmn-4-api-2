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

def check_bitlink(api_token, input_link):
  url_total='https://api-ssl.bitly.com/v4/bitlinks/{}'.format(input_link)
  headers_user = {'Authorization': 'Bearer ' + api_token}
  responce=requests.get(url_total, headers=headers_user)
  return responce.status_code

#url=input()
#bitlink=cut_url(token, url)
#if bitlink:
#  print(count_clicks(token, bitlink))
#else:
#  print('Your url is incorrect!')

#url='http://ya.ru'
url='http://bit.ly/2t7hCiD'
print(check_bitlink(token, url))
#print(count_clicks(token, url))
if check_bitlink(token, url)==404:
  print("1")
  print(cut_url(token, url))
elif (check_bitlink(token, url))==200:
  print("2")
  print('COUNT OF CLICKS: {}'.format(count_clicks(token, url)))
else:
  print("3")
  print('Your url is incorrect!')
