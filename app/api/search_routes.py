from flask import Blueprint, request
from flask_login import current_user, login_required
import json
from app.models import db, Solved, Problem, Review

search_routes = Blueprint("search", __name__)


@search_routes.route('/', methods=["GET"])
def get_problems():
    problems = Problem.query.all()
    print(problems)

    problems_list_ = []

    for problem in problems:
        problem_dict = problem.to_dict()

        problems_list_.append(
            {"problem_title": problem_dict['title'], "category": problem_dict['category', "difficulty": problem_dict["difficulty"]]})

    return {'search_types': problems_list_}
