from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.itempost import ItemPost, ItemPostSchema
from init import db
from blueprints.auth_bp import admin_or_owner_required

itempost_bp = Blueprint('itemposts', __name__, url_prefix='/item_posts')

# Get all item posts
@itempost_bp.route('/')
@jwt_required()
def all_item_posts():
    stmt = db.session.query(ItemPost).order_by(ItemPost.category_id)
    item_posts = db.session.execute(stmt).all()
    return ItemPostSchema(many=True).dump(item_posts)

# Get one item post
@itempost_bp.route('/<int:itempost_id>')
@jwt_required()
def one_item_post(itempost_id):
    stmt = db.session.query(ItemPost).filter_by(id=itempost_id)
    item_post = db.session.execute(stmt).scalar()
    if item_post:
        return ItemPostSchema().dump(item_post)
    else:
        return {'error': 'Item post not found'}, 404

# Create a new item post
@itempost_bp.route('/', methods=['POST'])
@jwt_required()
def create_item_post():
    item_post_info = ItemPostSchema().load(request.json)
    item_post = ItemPost(
        title=item_post_info['title'],
        description=item_post_info['description'],
        price=item_post_info['price'],
        user_id=get_jwt_identity(),
        category_id=item_post_info['category_id']
    )
    db.session.add(item_post)
    db.session.commit()
    return ItemPostSchema().dump(item_post), 201

# Update an item post
@itempost_bp.route('/<int:itempost_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_item_post(itempost_id):
    stmt = db.session.query(ItemPost).filter_by(id=itempost_id)
    item_post = db.session.execute(stmt).scalar()
    item_post_info = ItemPostSchema().load(request.json)
    if item_post:
        admin_or_owner_required(item_post.user.id)
        item_post.title = item_post_info.get('title', item_post.title)
        item_post.description = item_post_info.get('description', item_post.description)
        item_post.price = item_post_info.get('price', item_post.price)
        item_post.category_id = item_post_info.get('category_id', item_post.category_id)
        db.session.commit()
        return ItemPostSchema().dump(item_post)
    else:
        return {'error': 'Item not found'}, 404

# Delete an item post
@itempost_bp.route('/<int:itempost_id>', methods=['DELETE'])
@jwt_required()
def delete_item_post(itempost_id):
    stmt = db.session.query(ItemPost).filter_by(id=itempost_id)
    item_post = db.session.execute(stmt).scalar()
    if item_post:
        admin_or_owner_required(item_post.user.id)
        db.session.delete(item_post)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Item post not found'}, 404
