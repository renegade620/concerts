"""create test instances

Revision ID: 58fbb8ee5024
Revises: c468c19c3fa6
Create Date: 2024-09-25 02:25:49.506189

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58fbb8ee5024'
down_revision: Union[str, None] = 'c468c19c3fa6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
