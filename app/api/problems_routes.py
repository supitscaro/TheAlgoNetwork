from flask import Blueprint, jsonify
import json
from app.models import Problem

problems_routes = Blueprint("problems", __name__)


# Gets all array problems

@problems_routes.route('/<string:category>')
def get_problems(category):
    print(category)
    problems = Problem.query.filter(
        Problem.category == category.capitalize()).all()
    problems_dict_ = {}

    id = 0
    while id < len(problems):
        for problem in problems:
            problems_dict_[id] = problem.to_dict()
            id += 1

    return problems_dict_
