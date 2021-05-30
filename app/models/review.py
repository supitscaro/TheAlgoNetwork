from .db import db
# from .review import Review


class Review(db.Model):
    __tablename__ = 'reviews'

    # id, users_id, problems_id
    id = db.Column(db.Integer, primary_key=True)
    review_problems = db.Column(db.Boolean, nullable=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    problems_id = db.Column(db.Integer, db.ForeignKey(
        "problems.id"), nullable=False)

    user = db.relationship('User', foreign_keys=users_id)
    problem = db.relationship('Problem', foreign_keys=problems_id)

    def to_dict(self):
        return {
            "id": self.id,
            "review_problems": self.review_problems,
            "users_id": self.users_id,
            "problems_id": self.problems_id,
        }
