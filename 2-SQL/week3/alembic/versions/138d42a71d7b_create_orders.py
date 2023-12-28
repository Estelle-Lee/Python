"""create orders

Revision ID: 138d42a71d7b
Revises: 422d5e543b8e
Create Date: 2023-12-28 16:07:39.264689

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '138d42a71d7b'
down_revision: Union[str, None] = '422d5e543b8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE orders (
            id SERIAL PRIMARY KEY,
            dollar_amount_spent NUMERIC,
            customer_id INT NOT NULL,
            CONSTRAINT fk_orders_customers
                FOREIGN KEY(customer_id)
                REFERENCES customers(id)
                ON DELETE CASCADE
        );
        """
    )


def downgrade() -> None:
    op.execute(
        """
        DROP TABLE orders;
        """
    )
