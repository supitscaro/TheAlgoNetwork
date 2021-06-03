from flask import Blueprint, jsonify
import json
from app.models import Problem

problems_routes = Blueprint("problems", __name__)


# Gets all array problems

@problems_routes.route('/<string:category>')
def get_problems(category):
    problems = Problem.query.filter(
        Problem.category == category.capitalize()).all()
    problems_dict_ = {}

    id = 1
    while id < len(problems):
        for problem in problems:
            problems_dict_[id] = problem.to_dict()
            id += 1

    return problems_dict_


@problems_routes.route('/<string:category>/<int:id>')
def get_specific_problem(category, id):
    problems = Problem.query.filter(
        Problem.category == category.capitalize()).filter(Problem.id == id).all()

    problem_dict_ = {}

    problem_id = 0

    for problem in problems:
        problem_dict_[problem_id] = problem.to_dict()
        problem_id += 1

    return problem_dict_
