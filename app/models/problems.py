from .db import db


class Problems(db.Model):
    __tablename__ = 'problems'

    id = Column(db.Integer, primary_key=True)
    category = Column(db.String, nullable=False)
    difficulty = Column(db.String, nullable=False)
    title = Column(db.String, nullable=False)
    description = Column(db.String, nullable=False)
    solution = Column(db.String, nullable=False)
    solved = Column(db.Boolean, nullable=True)

    # assets = db.relationship("Asset", back_populates="problems")
    user = db.relationship("User", back_populates="problems")

    def to_dict(self):
        return {
            "id": self.id,
            "category": self.category,
            "difficulty": self.difficulty,
            "title": self.title,
            "description": self.description,
            "solution": self.solution,
            "solved": self.solved
        }
