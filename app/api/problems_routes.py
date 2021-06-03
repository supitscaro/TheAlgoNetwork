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

    for problem in problems:
        prob_to_add = problem.to_dict()
        problems_dict_[prob_to_add['id']] = prob_to_add

    return problems_dict_


@problems_routes.route('/<string:category>/<int:id>')
def get_specific_problem(category, id):
    problems = Problem.query.filter(
        Problem.category == category.capitalize()).filter(Problem.id == id).all()

    problem_dict_ = {}

    for problem in problems:
        prob_to_add = problem.to_dict()
        problem_dict_[prob_to_add['id']] = prob_to_add

    return problem_dict_
