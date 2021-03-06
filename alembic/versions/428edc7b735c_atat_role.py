"""atat role

Revision ID: 428edc7b735c
Revises: eafc7809ce2b
Create Date: 2018-06-29 12:24:09.787285

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '428edc7b735c'
down_revision = 'eafc7809ce2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('atat_role_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key('users_roles_fk', 'users', 'roles', ['atat_role_id'], ['id'])
    op.create_index('workspace_role_user_workspace', 'workspace_role', ['user_id', 'workspace_id'], unique=True)
    # ### end Alembic commands ###

    op.alter_column('roles', 'permissions', server_default='{}')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('workspace_role_user_workspace', table_name='workspace_role')
    op.drop_constraint('users_roles_fk', 'users', type_='foreignkey')
    op.drop_column('users', 'atat_role_id')
    # ### end Alembic commands ###

    op.alter_column('roles', 'permissions', server_default=None)
