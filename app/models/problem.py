from .db import db
from .problems_joins import solved
from .reviews_joined import review_problem


class Problem(db.Model):
    __tablename__ = 'problems'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    solution = db.Column(db.String, nullable=False)
    # reviews_id = db.Column(db.Boolean, nullable=True)
    solved = db.Column(db.Boolean, nullable=True)

    user = db.relationship("User", secondary=solved, back_populates="problems")
    reviews = db.relationship(
        "Review", secondary=review_problem, back_populates="problem")

    def to_dict(self):
        return {
            "id": self.id,
            "category": self.category,
            "difficulty": self.difficulty,
            "title": self.title,
            "description": self.description,
            "solution": self.solution,
            "review": self.review,
            "solved": self.solved
        }
