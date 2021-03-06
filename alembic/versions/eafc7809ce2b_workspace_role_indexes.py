"""workspace role indexes

Revision ID: eafc7809ce2b
Revises: d01a5b771012
Create Date: 2018-06-27 10:56:37.031326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eafc7809ce2b'
down_revision = 'd01a5b771012'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_roles_permissions'), 'roles', ['permissions'], unique=False, postgresql_using='gin')
    op.create_index(op.f('ix_workspace_role_user_id'), 'workspace_role', ['user_id'], unique=False)
    op.create_index(op.f('ix_workspace_role_workspace_id'), 'workspace_role', ['workspace_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_workspace_role_workspace_id'), table_name='workspace_role')
    op.drop_index(op.f('ix_workspace_role_user_id'), table_name='workspace_role')
    op.drop_index(op.f('ix_roles_permissions'), table_name='roles')
    # ### end Alembic commands ###
