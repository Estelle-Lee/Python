"""set date_of_birth default

Revision ID: 3da109565a0c
Revises: e43b4c4d87c3
Create Date: 2023-12-28 16:00:07.829562

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3da109565a0c'
down_revision: Union[str, None] = 'e43b4c4d87c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth SET DEFAULT now();
        """
    )


def downgrade() -> None:
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth DROP DEFAULT;
        """
    )
