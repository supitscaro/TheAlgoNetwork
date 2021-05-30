from .db import db
from .solved import Solved
from .review import Review


class Problem(db.Model):
    __tablename__ = 'problems'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    solution = db.Column(db.String, nullable=False)

    user = db.relationship("User", secondary=Solved, back_populates="problems")
    reviews = db.relationship("User", secondary=Review,
                              back_populates="reviews")

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
