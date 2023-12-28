"""create_table1_2_3

Revision ID: 5bd32e5c5387
Revises: a33aabca2d3c
Create Date: 2023-12-28 16:16:12.882122

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5bd32e5c5387'
down_revision: Union[str, None] = 'a33aabca2d3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE table1 (id SERIAL PRIMARY KEY);
        CREATE TABLE table2 (id SERIAL PRIMARY KEY);
        CREATE TABLE table3 (id SERIAL PRIMARY KEY);
        """
        )


def downgrade() -> None:
    op.execute(
        """
        DROP TABLE table3;
        DROP TABLE table2;
        DROP TABLE table1;
        """
    )
