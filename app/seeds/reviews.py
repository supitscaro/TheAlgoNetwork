from app.models import db, Review

# Adds a list of reviews for the demo user


def seed_reviews():
    review1 = Review(
        users_id=1,
        problems_id=2,
    )

    review2 = Review(
        users_id=1,
        problems_id=5,
    )

    review3 = Review(
        users_id=1,
        problems_id=20,
    )

    review4 = Review(
        users_id=1,
        problems_id=17,
    )

    review5 = Review(
        users_id=1,
        problems_id=12,
    )

    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)

    db.session.commit()


def undo_problems():
    db.session.execute('TRUNCATE problems;')
    db.session.commit()
