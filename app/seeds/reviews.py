from app.models import db, Review


def seed_reviews():

    review1 = Review(
        review_problems=True,
        users_id=1,
        problems_id=4
    )

    review2 = Review(
        review_problems=True,
        users_id=1,
        problems_id=12
    )

    review3 = Review(
        review_problems=True,
        users_id=1,
        problems_id=18
    )

    review4 = Review(
        review_problems=True,
        users_id=1,
        problems_id=19
    )

    review5 = Review(
        review_problems=True,
        users_id=1,
        problems_id=23
    )

    review6 = Review(
        review_problems=True,
        users_id=1,
        problems_id=26
    )


def undo_reviews():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY')
    db.session.commit()
