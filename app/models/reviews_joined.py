from .db import db


review_problem = db.Table(
    "review_problem", db.Model.metadata,
    db.Column("users_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("problems_id", db.Integer, db.ForeignKey("problems.id"))
)
