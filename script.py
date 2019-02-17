import requests
from requests.exceptions import RequestException
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def cut_url(api_token, input_link):
  url_shorten='https://api-ssl.bitly.com/v4/shorten'
  headers_user = {'Authorization': 'Bearer ' + api_token}
  input_link_params = urlparse(input_link)
  if input_link_params.scheme:
    json_url = {'long_url': input_link}
  else:
    json_url = {'long_url': 'http://' + input_link}
  response_post = requests.post(url_shorten, headers=headers_user, json=json_url)
  return response_post.json().get('id') 

def count_clicks(api_token, input_link):
  url = urlparse(input_link).netloc + urlparse(input_link).path
  url_total='https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(url)
  payload={"units": -1}
  headers_user = {'Authorization': 'Bearer ' + api_token}
  response=requests.get(url_total, headers=headers_user, params=payload)
  return response.json()["total_clicks"] 

def check_bitlink(api_token, input_link):
  url = urlparse(input_link).netloc + urlparse(input_link).path
  url_total='https://api-ssl.bitly.com/v4/bitlinks/{}'.format(url)
  headers_user = {'Authorization': 'Bearer ' + api_token}
  response=requests.get(url_total, headers=headers_user)
  return response.ok

def check_url(input_link):
  try:
    url = 'http://' + urlparse(input_link).netloc + urlparse(input_link).path
    response=requests.get(url)
    return response.ok
  except RequestException:
    return False

if __name__ == "__main__":
  load_dotenv()
  token=os.getenv("TOKEN")
  
  url = input('Enter url: ')

  if not(check_url(url)):
    print('Invalid url!')
  elif check_bitlink(token, url):
    print('The number of clicks on the link: {}'.format(count_clicks(token, url)))
  else:
    print('Your bitlink: {}'.format(cut_url(token, url)))
