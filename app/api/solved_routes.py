from flask import Blueprint, request
from flask_login import current_user, login_required
import json
from app.models import db, Solved, Problem

solved_routes = Blueprint("solved", __name__)


# get user's solved list
@solved_routes.route('/<int:user_id>', methods=["GET"])
@login_required
def get_solvedlist(user_id):

    solved = Solved.query.filter(Solved.users_id == user_id).all()

    solved_dict_ = {}

    problems_dict = {}

    for item in solved:
        solved_items = item.to_dict()
        problem_solved = solved_items['problems_id']
        new_problems = Problem.query.filter(Problem.id == problem_solved).all()

        for problem in new_problems:
            prob_solved = problem.to_dict()
            problems_dict[prob_solved['id']] = prob_solved

    return problems_dict


# add problem to user's solved list
@solved_routes.route('/<int:problemId>/<int:userId>', methods=["POST"])
@login_required
def add_to_solved(problemId, userId):

    new_solved = Solved(
        problem_solved=True,
        users_id=userId,
        problems_id=problemId
    )

    db.session.add(new_solved)
    db.session.commit()

    res = new_solved.to_dict()

    return res


# remove problem from user's review list
@solved_routes.route('/<int:problemId>', methods=["DELETE"])
@login_required
def delete_solved(problemId):
    problems = Solved.query.filter(Solved.problems_id == problemId).all()

    for problem in problems:
        specific_problem = problem.to_dict()
    db.session.delete(problem)
    db.session.commit()

    return problem.to_dict()
