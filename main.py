from flask import Flask, request, render_template

from api.logger import get_logger
from api.views import api_bp
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_post_by_user

app = Flask(__name__)

main_logger = get_logger('main_logger')


@app.route('/')
def all_posts():
    """Главная страница - все посты"""
    posts = get_posts_all()
    main_logger.info("main")
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:postid>')
def get_comments_by_postid(postid):
    """Пост по его номеру"""
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', comments=comments, post=post)


@app.route('/search/', methods=['GET'])
def search_posts_by_word():
    """представление для поиска по маршруту GET /search/?s=... 10 постов, если есть,
    по вхождению ключевого слова в текст поста, регистрозависимость"""
    search_query = request.args.get('s', '')
    finded_posts = search_for_posts(search_query)
    posts = finded_posts[:10]
    return render_template('search.html', search_word=search_query, posts=posts)


@app.route('/users/<user_name>', methods=['GET'])
def search_posts_by_user(user_name):
    """представление с выводом постов конкретного пользователя GET /users/<username>
    шаблон user-feed"""
    posts = get_post_by_user(user_name)
    return render_template('user-feed.html', posts=posts)


app.register_blueprint(api_bp)
app.config['JSON_AS_ASCII'] = False


@app.errorhandler(404)
def page_not_found(error):
    """Ошибка на несуществующие старницы"""
    return "404 - Страница не найдена"

@app.errorhandler(500)
def internal_error(error):
    return "500 - Внутренняя ошибка"


if __name__ == '__main__':
    app.run(debug=True)
