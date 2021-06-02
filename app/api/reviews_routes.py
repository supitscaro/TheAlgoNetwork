from flask import Blueprint, jsonify
from flask_login import current_user, login_required
import json
from app.models import Review

reviews_routes = Blueprint("reviews", __name__)

# get user's review list


# @login_required
@reviews_routes.route('/', methods=["GET", "POST"])
def get_reviewlist():
    user_id = current_user.id
    reviews = Review.query.filter(Review.users_id == 1).all()
    return {'test': 'code'}
