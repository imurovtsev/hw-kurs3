from utils import get_posts_all
import pytest


def test_get_posts_all():
    assert type(get_posts_all()) == list
    assert get_posts_all()[0]["poster_name"] == 'leo'
    assert get_posts_all() != []
# print(get_posts_all())
# print(get_post_by_user('johnny'))
# print(get_comments_by_post_id(1111))
# print(search_for_posts('кот'))
# print(get_post_by_pk(111))
