from authorisation import get_reddit_auth_headers, get_reddit_auth_token
import config_auth
import logging
from make_data_requests import make_all_comments_request, make_top_subreddit_requests, take_subreddit_and_all_its_comments
import requests
from show_data import show_all_posts
from typing import TypedDict



if __name__ == "__main__":
        
        TOKEN = get_reddit_auth_token()
        headers = get_reddit_auth_headers(TOKEN)

        print(f"{type(headers) = }")

        number_of_news = int(input("Введите количество топ-новостей: "))

        result_subreddit = make_top_subreddit_requests(number_of_news, headers)
        show_all_posts(result_subreddit, number_of_news)
        comments_url_list = make_all_comments_request(result_subreddit, headers)
        take_subreddit_and_all_its_comments(comments_url_list, headers)