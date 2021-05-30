from flask import Blueprint, jsonify
import json
from app.models import Problem

problems_routes = Blueprint("problems", __name__)


# Gets all array problems

@problems_routes.route('/arrays/<arrays>')
def get_arrays_problems(arrays):
    arrays_problems = Problem.query.filter(Problem.category == 'Arrays').all()

    arrays_dict_ = {}

    id = 0
    while id < len(arrays_problems):
        for problem in arrays_problems:
            arrays_dict_[id] = problem.to_dict()
            id += 1

    return arrays_dict_


# Gets all strings problems
@problems_routes.route('/strings/<strings>')
def get_strings_problems(strings):
    strings_problems = Problem.query.filter(
        Problem.category == 'Strings').all()

    strings_dict_ = {}

    id = 0
    while id < len(strings_problems):
        for problem in strings_problems:
            strings_dict_[id] = problem.to_dict()
            id += 1

    return strings_dict_


# Gets all trees problems
@problems_routes.route('/trees/<trees>')
def get_trees_problems(trees):
    trees_problems = Problem.query.filter(
        Problem.category == 'Trees').all()

    trees_dict_ = {}

    id = 0
    while id < len(trees_problems):
        for problem in trees_problems:
            trees_dict_[id] = problem.to_dict()
            id += 1

    return trees_dict_


# Gets all hash tables problems
@problems_routes.route('/hash/<hash>')
def get_hash_problems(hash):
    hash_problems = Problem.query.filter(
        Problem.category == 'Hash Tables').all()

    hash_dict_ = {}

    id = 0
    while id < len(hash_problems):
        for problem in hash_problems:
            hash_dict_[id] = problem.to_dict()
            id += 1

    return hash_dict_
