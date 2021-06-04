from .db import db


class Solved(db.Model):
    __tablename__ = 'solved'

    id = db.Column(db.Integer, primary_key=True)
    problem_solved = db.Column(db.Boolean, nullable=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    problems_id = db.Column(db.Integer, db.ForeignKey(
        "problems.id"), nullable=False)

    user = db.relationship('User', foreign_keys=users_id)
    problem = db.relationship('Problem', foreign_keys=problems_id)

    def to_dict(self):
        return {
            "id": self.id,
            "problem_solved": self.problems_id,
            "users_id": self.users_id,
            "problems_id": self.problems_id
        }
