"""rename date_of_birth to dob

Revision ID: 422d5e543b8e
Revises: 3da109565a0c
Create Date: 2023-12-28 16:05:01.652317

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '422d5e543b8e'
down_revision: Union[str, None] = '3da109565a0c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        ALTER TABLE customers
        RENAME COLUMN date_of_birth TO dob;
        """
    )


def downgrade() -> None:
    op.execute(
        """
        ALTER TABLE customers
        RENAME COLUMN dob TO date_of_birth;
        """
    )
