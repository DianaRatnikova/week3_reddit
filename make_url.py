import config_auth
import requests


def construct_comments_url(result_subreddit: requests.models.Response) -> list:
    comments_url_list = []
    for post in result_subreddit.json()["data"]["children"]:
        comments_url = config_auth.CONST_URL + post['data']['permalink']
        comments_url = comments_url[:-1]+'.json?sort=new'
        comments_url_list.append(comments_url)
    return comments_url_list
