import requests


def show_all_posts(result_subreddit: requests.models.Response, limit: int) -> None:
    for num_of_post in range(limit):
        print(f"{result_subreddit.json()['data']['children'][num_of_post]['data']['title'] = } \n")