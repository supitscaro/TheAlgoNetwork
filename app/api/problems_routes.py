from flask import Blueprint, jsonify
import json
from flask_login import login_required
from app.models import db, Problem, Solved, Review

problems_routes = Blueprint("problems", __name__)


# Gets all array problems
@problems_routes.route('/<string:category>')
@login_required
def get_problems(category):
    problems = Problem.query.filter(
        Problem.category == category.capitalize()).all()
    problems_dict_ = {}

    for problem in problems:
        prob_to_add = problem.to_dict()
        problems_dict_[prob_to_add['id']] = prob_to_add

    return problems_dict_


# get specific problems for each category
@problems_routes.route('/<string:category>/<int:id>')
@login_required
def get_specific_problem(category, id):
    problems = Problem.query.filter(
        Problem.category == category.capitalize()).filter(Problem.id == id).all()

    problem_dict_ = {}

    for problem in problems:
        prob_to_add = problem.to_dict()
        problem_dict_[prob_to_add['id']] = prob_to_add

    return problem_dict_


@problems_routes.route('/')
@login_required
def get_all_problems():
    problems = Problem.query.all()

    all_problems_ = {}

    for problem in problems:
        problem_to_add = problem.to_dict()
        all_problems_[problem_to_add['id']] = problem_to_add

    return all_problems_
