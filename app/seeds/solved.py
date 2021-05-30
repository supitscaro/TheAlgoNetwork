from app.models import db, Problem, User, Solved


def seed_solved():

    user1 = User.query.get(1)
    problem1 = Problem.query.get(1)
    solved1 = Solved(problem_solved=True, users_id=user1.id,
                     problems_id=problem1.id)

    db.session.add(solved1)
    db.session.commit()


def undo_solved():
    db.session.execute('TRUNCATE solved RESTART IDENTITY')
    db.session.commit()
