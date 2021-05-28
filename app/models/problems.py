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
