from flask import Blueprint, request
from flask_login import current_user, login_required
import json
from app.models import db, Solved, Problem, Review

search_routes = Blueprint("search", __name__)


@search_routes.route('/', methods=["GET"])
def get_problems():
    problems = Problem.query.all()
    print(problems)

    problems_dict_ = {}

    for problem in problems:
        problem_dict = problem.to_dict()
        problems_dict_[problem_dict['id']] = problem_dict

    return problems_dict_
