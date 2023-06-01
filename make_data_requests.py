import requests
from make_url import construct_comments_url
from authorisation import Headers

def make_top_subreddit_requests(limit: int, headers: Headers) -> requests.models.Response:
    result_subreddit = requests.get(f'https://oauth.reddit.com/top.json?limit={limit}', headers=headers)
    return result_subreddit



def make_one_subreddit_request(comment_url, num_of_file, headers):
    result_comments = requests.get(f'{comment_url}', headers=headers)

    # ВОПРОС: строкой ниже написан коммент, который никак не привязан к названию переменных/функций
    # и позволяет вспомнить, почему вообще тут используется [0]. Неужели даже это луччше не писать? (

    # нулевой элемент списка содержит инфу о посте, первый - все комменты
    one_subreddit_json = result_comments.json()[0]['data']['children']
    return one_subreddit_json


def make_one_comment_request(comment_url, num_of_post, headers):
    result_comments = requests.get(f'{comment_url}', headers=headers)
    # нулевой элемент списка содержит инфу о посте, первый - все комменты
    comment_json = result_comments.json()[1]['data']['children']
    return comment_json



def make_all_comments_request(result_subreddit: requests.models.Response, headers: str):
    comments_url_list = construct_comments_url(result_subreddit)
    print(f"{comments_url_list = }")
    for (num_of_post, comment_url) in enumerate(comments_url_list):
        comment_json = make_one_comment_request(comment_url, num_of_post, headers)
        one_subreddit_json = make_one_subreddit_request(comment_url, num_of_post, headers)
    # допилю функцию, определившись, что из этого json'a мне нужнее возвращать