"""create test instances

Revision ID: aaaca6e17013
Revises: 58fbb8ee5024
Create Date: 2024-09-25 02:28:29.982416

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aaaca6e17013'
down_revision: Union[str, None] = '58fbb8ee5024'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
