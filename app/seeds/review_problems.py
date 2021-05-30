from app.models import db, Review_Problem


def seed_review_problems():

    review1 = Solved(
        review_problems=True,
        users_id=1,
        problems_id=4
    )

    review2 = Solved(
        review_problems=True,
        users_id=1,
        problems_id=12
    )

    review3 = Solved(
        review_problems=True,
        users_id=1,
        problems_id=18
    )

    review4 = Solved(
        review_problems=True,
        users_id=1,
        problems_id=19
    )

    review5 = Solved(
        review_problems=True,
        users_id=1,
        problems_id=23
    )

    review6 = Solved(
        review_problems=True,
        users_id=1,
        problems_id=26
    )


def undo_review_problems():
    db.session.execute('TRUNCATE review_problems RESTART IDENTITY')
    db.session.commit()
