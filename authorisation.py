import config_auth
import requests
from typing import TypedDict



class Headers(TypedDict):
    UserAgent: str 
    Authorization: str


def get_reddit_auth_token() -> str:

    data = {'grant_type': 'password',
        'username': config_auth.user_name,
        'password': config_auth.password}

    auth = requests.auth.HTTPBasicAuth(config_auth.CLIENT_ID, config_auth.SECRET_TOKEN)
    result_post = requests.post(config_auth.URL_ACCESS_TOKEN,
                                auth=auth, 
                                data=data, 
                                headers=config_auth.HEADERS_INFO)
    TOKEN = result_post.json()['access_token']
    return TOKEN


def get_reddit_auth_headers(TOKEN: str) -> Headers:
    headers =  config_auth.HEADERS_INFO | {'Authorization': f"bearer {TOKEN}"}
    return headers