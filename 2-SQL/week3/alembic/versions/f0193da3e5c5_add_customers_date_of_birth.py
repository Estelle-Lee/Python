"""add customers date_of_birth

Revision ID: f0193da3e5c5
Revises: 4ea4ac08f5d5
Create Date: 2023-12-28 15:24:04.808835

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0193da3e5c5'
down_revision: Union[str, None] = '4ea4ac08f5d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# def upgrade() -> None:
#     pass


# def downgrade() -> None:
#     pass

def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )


