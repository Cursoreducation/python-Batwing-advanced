"""001_create_users

Revision ID: df432fb086b2
Revises: 
Create Date: 2022-07-12 22:43:39.366250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df432fb086b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("email", sa.String(300), nullable=False, unique=True),
        sa.Column("first_name", sa.String(300), nullable=False),
        sa.Column("last_name", sa.String(300), nullable=False),
        sa.Column("password", sa.String(300), nullable=False)
    )


def downgrade() -> None:
    pass
