from authorisation import get_reddit_auth_headers, get_reddit_auth_token
import config_auth
import logging
from make_data_requests import make_all_comments_request, make_top_subreddit_requests
import requests

from show_data import show_all_posts
from typing import TypedDict



if __name__ == "__main__":
        
        TOKEN = get_reddit_auth_token()
        headers = get_reddit_auth_headers(TOKEN)

        print(f"{type(headers) = }")

        limit= int(input("Введите количество топ-новостей: "))

        result_subreddit = make_top_subreddit_requests(limit, headers)
        show_all_posts(result_subreddit, limit)
        logging.info('make_all_comments_request(result_subreddit, headers)')
        make_all_comments_request(result_subreddit, headers)
