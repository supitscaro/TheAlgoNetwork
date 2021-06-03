from flask import Blueprint, request
from flask_login import current_user, login_required
import json
from app.models import db, Review, Problem

reviews_routes = Blueprint("reviews", __name__)


# get user's review list
@reviews_routes.route('/<int:user_id>', methods=["GET"])
@login_required
def get_reviewlist(user_id):

    reviews = Review.query.filter(Review.users_id == user_id).all()

    id = 1

    reviews_dict_ = {}

    problems_dict = {}

    for item in reviews:
        review_items = item.to_dict()
        problem_review = review_items['problems_id']
        new_problems = Problem.query.filter(Problem.id == problem_review).all()

        for problem in new_problems:
            problems_dict[id] = problem.to_dict()
            id += 1

    return problems_dict


# add problem to user's review list
@reviews_routes.route('/<int:problemId>/<int:userId>', methods=["POST"])
@login_required
def add_to_review(problemId, userId):
    print('butt', problemId)
    add_problem = Problem.query.get(problemId)

    new_review = Review(
        review_problems=True,
        users_id=userId,
        problems_id=problemId
    )

    db.session.add(new_review)
    db.session.commit()

    res = new_review.to_dict()

    return res
