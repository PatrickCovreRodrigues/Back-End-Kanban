"""delete table todo

Revision ID: 9141774fc487
Revises: be7ee79b5bcc
Create Date: 2025-01-02 09:56:03.714403

"""
from typing import Sequence, Union
import sqlalchemy as sa

from alembic import op



# revision identifiers, used by Alembic.
revision: str = '9141774fc487'
down_revision: Union[str, None] = 'be7ee79b5bcc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
