from app.models import db, Solved


def seed_solved():

    problem1 = Solved(
        problem_solved=True,
        users_id=1,
        problems_id=2
    )

    problem2 = Solved(
        problem_solved=True,
        users_id=1,
        problems_id=20
    )

    problem3 = Solved(
        problem_solved=True,
        users_id=1,
        problems_id=14
    )

    problem4 = Solved(
        problem_solved=True,
        users_id=1,
        problems_id=10
    )

    problem5 = Solved(
        problem_solved=True,
        users_id=1,
        problems_id=24
    )

    problem6 = Solved(
        problem_solved=True,
        users_id=1,
        problems_id=29
    )

    problem7 = Solved(
        problem_solved=True,
        users_id=1,
        problems_id=31
    )

    problem8 = Solved(
        problem_solved=True,
        users_id=1,
        problems_id=35
    )

    problem9 = Solved(
        problem_solved=True,
        users_id=1,
        problems_id=37
    )

    problem10 = Solved(
        problem_solved=True,
        users_id=1,
        problems_id=40
    )

    db.session.add(problem1)
    db.session.add(problem2)
    db.session.add(problem3)
    db.session.add(problem4)
    db.session.add(problem5)
    db.session.add(problem6)
    db.session.add(problem7)
    db.session.add(problem8)
    db.session.add(problem9)
    db.session.add(problem10)

    db.session.commit()


def undo_solved():
    db.session.execute('TRUNCATE solved RESTART IDENTITY')
    db.session.commit()
