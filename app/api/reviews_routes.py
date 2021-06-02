from flask import Blueprint, jsonify
from flask_login import current_user, login_required
import json
from app.models import Review

reviews_routes = Blueprint("reviews", __name__)

# get user's review list


@reviews_routes.route('/', methods=["GET", "POST"])
@login_required
def get_reviewlist():
    reviews = Review.query.filter(Review.users_id == current_user.id)
    print('butthole', reviews)
    pass
