"""add default atat role

Revision ID: 58115a0c85ac
Revises: 428edc7b735c
Create Date: 2018-07-19 17:13:32.881309

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm.session import Session

from authz.models.role import Role
from authz.models.permissions import Permissions

# revision identifiers, used by Alembic.
revision = '58115a0c85ac'
down_revision = '428edc7b735c'
branch_labels = None
depends_on = None


def upgrade():
    session = Session(bind=op.get_bind())
    mission_owner_role = Role(
        name='default',
        description='',
        permissions=[
            Permissions.REQUEST_JEDI_WORKSPACE,
        ]
    )
    session.add(mission_owner_role)
    session.commit()


def downgrade():
    db = op.get_bind()
    db.execute("DELETE FROM roles WHERE name = 'default'")
