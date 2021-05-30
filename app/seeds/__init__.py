from flask.cli import AppGroup
from .users import seed_users, undo_users
from .problems import seed_problems, undo_problems
from .reviews import seed_reviews, undo_reviews
# from .review_problems import seed_review_problems, undo_review_problems
from .solved import seed_solved, undo_solved

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_problems()
    seed_reviews()
    seed_solved()
    # Add other seed functions here

# Creates the `flask seed undo` command


@seed_commands.command('undo')
def undo():
    undo_users()
    undo_problems()
    undo_reviews()
    undo_solved()
    # Add other undo functions here
