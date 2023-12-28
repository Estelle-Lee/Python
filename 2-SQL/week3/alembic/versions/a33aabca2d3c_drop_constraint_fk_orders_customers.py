"""drop constraint fk_orders_customers

Revision ID: a33aabca2d3c
Revises: 138d42a71d7b
Create Date: 2023-12-28 16:12:30.440610

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a33aabca2d3c'
down_revision: Union[str, None] = '138d42a71d7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        ALTER TABLE orders
        DROP CONSTRAINT fk_orders_customers;
        """
    )


def downgrade() -> None:
    op.execute(
        """
        ALTER TABLE orders
        ADD CONSTRAINT fk_orders_customers
        FOREIGN KEY (customer_id)
        REFERENCES customers(id)
        ON DELETE CASCADE;
        """
        )
