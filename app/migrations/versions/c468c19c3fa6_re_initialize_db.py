"""re-initialize db

Revision ID: c468c19c3fa6
Revises: 8a45ca2e91d4
Create Date: 2024-09-25 02:09:39.308881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c468c19c3fa6'
down_revision: Union[str, None] = '8a45ca2e91d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
