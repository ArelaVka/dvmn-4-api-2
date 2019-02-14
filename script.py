import requests
from requests.exceptions import RequestException
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def cut_url(api_token, long_url):
  url_shorten='https://api-ssl.bitly.com/v4/shorten'
  headers_user = {'Authorization': 'Bearer ' + api_token}
  json_url = {'long_url': long_url}
  response_post = requests.post(url_shorten, headers=headers_user, json=json_url)
  return response_post.json().get('id') 

def count_clicks(api_token, bitlink):
  url_total='https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(bitlink)
  payload={"units": -1}
  headers_user = {'Authorization': 'Bearer ' + api_token}
  response=requests.get(url_total, headers=headers_user, params=payload)
  return response.json()["total_clicks"] 

def check_bitlink(api_token, input_link):
  url_total='https://api-ssl.bitly.com/v4/bitlinks/{}'.format(input_link)
  headers_user = {'Authorization': 'Bearer ' + api_token}
  response=requests.get(url_total, headers=headers_user)
  return response.ok

def check_http_bitlink(api_token, input_link):
  url_total='https://api-ssl.bitly.com/v4/bitlinks/{}'.format(input_link[7:])
  headers_user = {'Authorization': 'Bearer ' + api_token}
  response=requests.get(url_total, headers=headers_user)
  return response.ok

def check_url(input_link):
  try:
    response=requests.get('http://' + url)
    return response.ok
  except RequestException:
    return False

def check_http_url(input_link):
  try:
    response=requests.get(url)
    return response.ok
  except RequestException:
    return False

if __name__ == "__main__":
  load_dotenv()
  token=os.getenv("TOKEN")
  
  url = input('Enter url: ')

  if not(check_url(url)) and not(check_http_url(url)):
    print('Invalid url!')
  elif check_http_bitlink(token, url):
    print('22222')
    print('The number of clicks on the link : {}'.format(count_clicks(token, url[7:])))
  elif check_bitlink(token, url):
    print('The number of clicks on the link: {}'.format(count_clicks(token, url)))
  elif check_http_url(url):
    print('Your bitlink: {}'.format(cut_url(token, url)))
  elif check_url(url):
    print('Your bitlink: {}'.format(cut_url(token, 'http://' + url)))
