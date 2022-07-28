import json
from json import JSONDecodeError
from exceptions.data_exceptions import DataSourceError

def get_posts_all() -> list[dict]:
    """Возвращает все доступные посты"""
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        raise DataSourceError('Не удается получить данные из файла data.json')
    return data


def get_post_by_user(user_name) -> list[dict]:
    """Возвращает посты конкретного пользователя, должна вызывать
    ошибку ValueError если такого пользователя нет и пустой список,
    если у пользователя нет постов"""
    all_posts = get_posts_all()
    user_posts = []
    for post in all_posts:
        if post['poster_name'] == user_name:
            user_posts.append(post)
    if len(user_posts) < 1:
        raise ValueError(f"По имени {user_name} не найдено ни одного поста")
    return user_posts


def get_comments_by_post_id(post_id: int) -> list[dict]:
    """Возвращает комментарии определенного поста, должна вызывать
    ошибку ValueError если такого поста нет и пустой список, если у
    поста нет комментов"""
    with open('comments.json', 'r', encoding='utf8') as file:
        all_comments = json.load(file)
    comments = []
    for comment in all_comments:
        if comment['post_id'] == post_id:
            comments.append(comment)
    if len(comments) < 1:
        raise ValueError(f"По id поста {post_id} не найдено комментариев")
    return comments



def search_for_posts(query) -> list[dict]:
    """возвращает список постов по ключевому слову"""
    all_posts = get_posts_all()
    posts = []
    for post in all_posts:
        if query.lower() in post['content'].lower():
            posts.append(post)
    return posts


def get_post_by_pk(pk: int) -> dict:
    """возвращает один пост по его идентификатору"""
    all_posts = get_posts_all()
    for post in all_posts:
        if post["pk"] == pk:
            return post
    raise ValueError(f"Нет такого поста по id {pk}")


#print(type(get_posts_all()))
#print(get_posts_all())
#print(get_post_by_user('johnny'))
#print(get_comments_by_post_id(1))
#print(search_for_posts('тарелка'))
#print(get_post_by_pk(1))