from .db import db


class Review(db.Model):
    __tablename__ = 'reviews'

    # id, users_id, problems_id
    id = Column(db.Integer, primary_key=True)
    users_id = Column(db.Integer, nullable=False)
    problems_id = Column(db.Integer, nullable=False)

    user = db.relationship("User", back_populates="reviews")
    problem = db.relationship("Problem", back_populates="reviews")

    def to_dict(self):
        return {
            "id": self.id,
            "users_id": self.users_id,
            "problems_id": self.problems_id,
        }
