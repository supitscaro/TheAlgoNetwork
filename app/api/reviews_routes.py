from flask import Blueprint, request
from flask_login import current_user, login_required
import json
from app.models import Review, Problem

reviews_routes = Blueprint("reviews", __name__)


# get user's review list
@reviews_routes.route('/<int:user_id>', methods=["GET", "POST"])
@login_required
def get_reviewlist(user_id):

    reviews = Review.query.filter(Review.users_id == user_id).all()

    reviews_dict_ = {}

    id = 0

    for item in reviews:
        review_items = item.to_dict()
        problem_review = review_items['problems_id']

    problems_to_review = Problem.query.filter(
        Problem.id == problem_review).all()

    for problem in problems_to_review:
        reviews_dict_[id] = problem.to_dict()

    return reviews_dict_


# add problem to user's review list
@reviews_routes.route('/<int:id>', methods=["POST"])
def add_to_review(id):
    data = request.get_json()

    # ??
    new_review = Review(
        review_prob
    )
