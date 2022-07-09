"""002_create_group_table

Revision ID: 002_create_group_table
Revises: 001_create_user_table
Create Date: 2022-07-01 17:06:32.545523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_create_group_table'
down_revision = '001_create_user_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "group",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(300), nullable=False, unique=True),
        sa.Column("description", sa.String(300), nullable=False),
    )
    op.add_column("user", sa.Column("group_id", sa.Integer, sa.ForeignKey("group.id")))


def downgrade() -> None:
    op.drop_table("group")
    op.drop_column("user", "group_id")
