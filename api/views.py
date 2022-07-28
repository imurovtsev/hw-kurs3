from flask import Blueprint, jsonify

from api.logger import get_logger
from utils import get_posts_all, get_post_by_pk

logger = get_logger('api_logger')

api_bp = Blueprint('api', __name__)


@api_bp.route('/api/posts')
def get_json_posts():
    posts = get_posts_all()
    logger.info('get_json_posts')
    return jsonify(posts)


@api_bp.route('/api/posts/<int:post_id>')
def get_json_post_by_id(post_id):
    post = get_post_by_pk(post_id)
    logger.info(f'get_json_post_by_id {post_id}')
    return jsonify(post)
