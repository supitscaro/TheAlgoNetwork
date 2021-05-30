from app.models import db, Problem, User, Review


def seed_reviews():

    user1 = User.query.get(1)
    problem1 = Problem.query.get(1)
    review1 = Review(review_problems=True, users_id=user1.id,
                     problems_id=problem1.id)

    db.session.add(review1)
    db.session.commit()


def undo_reviews():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY')
    db.session.commit()
