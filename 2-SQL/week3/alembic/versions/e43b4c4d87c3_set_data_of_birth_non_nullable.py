"""set data_of_birth non_nullable

Revision ID: e43b4c4d87c3
Revises: f0193da3e5c5
Create Date: 2023-12-28 15:53:20.917449

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e43b4c4d87c3'
down_revision: Union[str, None] = 'f0193da3e5c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth SET NOT NULL;
        """
    )


def downgrade() -> None:
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth DROP NOT NULL;
        """
    )
