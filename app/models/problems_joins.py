from .db import db


solved = db.Table(
    "solved", db.Model.metadata,
    db.Column("solved_problem", db.Boolean, nullable=True),
    db.Column("users_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("problems_id", db.Integer, db.ForeignKey("problems.id"))
)
