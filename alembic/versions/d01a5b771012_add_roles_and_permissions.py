"""add roles and permissions

Revision ID: d01a5b771012
Revises: 1e7539dfa021
Create Date: 2018-06-26 15:16:00.742957

"""
import os
import sys

from alembic import op
from sqlalchemy.orm.session import Session

# Add project root to python path so we can import models
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(project_root)

from authz.models.role import Role
from authz.models.permissions import Permissions


# revision identifiers, used by Alembic.
revision = 'd01a5b771012'
down_revision = '1e7539dfa021'
branch_labels = None
depends_on = None


def upgrade():
    session = Session(bind=op.get_bind())
    roles = [
        Role(
            name='ccpo',
            description='',
            permissions=[
                Permissions.VIEW_ORIGINAL_JEDI_REQEUST,
                Permissions.REVIEW_AND_APPROVE_JEDI_WORKSPACE_REQUEST,
                Permissions.MODIFY_ATAT_ROLE_PERMISSIONS,
                Permissions.CREATE_CSP_ROLE,
                Permissions.DELETE_CSP_ROLE,
                Permissions.DEACTIVE_CSP_ROLE,
                Permissions.MODIFY_CSP_ROLE_PERMISSIONS,

                Permissions.VIEW_USAGE_REPORT,
                Permissions.VIEW_USAGE_DOLLARS,
                Permissions.ADD_AND_ASSIGN_CSP_ROLES,
                Permissions.REMOVE_CSP_ROLES,
                Permissions.REQUEST_NEW_CSP_ROLE,
                Permissions.ASSIGN_AND_UNASSIGN_ATAT_ROLE,

                Permissions.VIEW_ASSIGNED_ATAT_ROLE_CONFIGURATIONS,
                Permissions.VIEW_ASSIGNED_CSP_ROLE_CONFIGURATIONS,

                Permissions.DEACTIVATE_WORKSPACE,
                Permissions.VIEW_ATAT_PERMISSIONS,
                Permissions.TRANSFER_OWNERSHIP_OF_WORKSPACE,

                Permissions.ADD_APPLICATION_IN_WORKSPACE,
                Permissions.DELETE_APPLICATION_IN_WORKSPACE,
                Permissions.DEACTIVATE_APPLICATION_IN_WORKSPACE,
                Permissions.VIEW_APPLICATION_IN_WORKSPACE,
                Permissions.RENAME_APPLICATION_IN_WORKSPACE,

                Permissions.ADD_ENVIRONMENT_IN_APPLICATION,
                Permissions.DELETE_ENVIRONMENT_IN_APPLICATION,
                Permissions.DEACTIVATE_ENVIRONMENT_IN_APPLICATION,
                Permissions.VIEW_ENVIRONMENT_IN_APPLICATION,
                Permissions.RENAME_ENVIRONMENT_IN_APPLICATION,

                Permissions.ADD_TAG_TO_WORKSPACE,
                Permissions.REMOVE_TAG_FROM_WORKSPACE
            ]
        ),
        Role(
            name='owner',
            description='',
            permissions=[
                Permissions.REQUEST_JEDI_WORKSPACE,
                Permissions.VIEW_ORIGINAL_JEDI_REQEUST,

                Permissions.VIEW_USAGE_REPORT,
                Permissions.VIEW_USAGE_DOLLARS,
                Permissions.ADD_AND_ASSIGN_CSP_ROLES,
                Permissions.REMOVE_CSP_ROLES,
                Permissions.REQUEST_NEW_CSP_ROLE,
                Permissions.ASSIGN_AND_UNASSIGN_ATAT_ROLE,

                Permissions.VIEW_ASSIGNED_ATAT_ROLE_CONFIGURATIONS,
                Permissions.VIEW_ASSIGNED_CSP_ROLE_CONFIGURATIONS,

                Permissions.DEACTIVATE_WORKSPACE,
                Permissions.VIEW_ATAT_PERMISSIONS,
                Permissions.TRANSFER_OWNERSHIP_OF_WORKSPACE,

                Permissions.ADD_APPLICATION_IN_WORKSPACE,
                Permissions.DELETE_APPLICATION_IN_WORKSPACE,
                Permissions.DEACTIVATE_APPLICATION_IN_WORKSPACE,
                Permissions.VIEW_APPLICATION_IN_WORKSPACE,
                Permissions.RENAME_APPLICATION_IN_WORKSPACE,

                Permissions.ADD_ENVIRONMENT_IN_APPLICATION,
                Permissions.DELETE_ENVIRONMENT_IN_APPLICATION,
                Permissions.DEACTIVATE_ENVIRONMENT_IN_APPLICATION,
                Permissions.VIEW_ENVIRONMENT_IN_APPLICATION,
                Permissions.RENAME_ENVIRONMENT_IN_APPLICATION,
            ]
        ),
        Role(
            name='admin',
            description='',
            permissions=[
                Permissions.VIEW_USAGE_REPORT,
                Permissions.ADD_AND_ASSIGN_CSP_ROLES,
                Permissions.REMOVE_CSP_ROLES,
                Permissions.REQUEST_NEW_CSP_ROLE,
                Permissions.ASSIGN_AND_UNASSIGN_ATAT_ROLE,

                Permissions.VIEW_ASSIGNED_ATAT_ROLE_CONFIGURATIONS,
                Permissions.VIEW_ASSIGNED_CSP_ROLE_CONFIGURATIONS,

                Permissions.ADD_APPLICATION_IN_WORKSPACE,
                Permissions.DELETE_APPLICATION_IN_WORKSPACE,
                Permissions.DEACTIVATE_APPLICATION_IN_WORKSPACE,
                Permissions.VIEW_APPLICATION_IN_WORKSPACE,
                Permissions.RENAME_APPLICATION_IN_WORKSPACE,

                Permissions.ADD_ENVIRONMENT_IN_APPLICATION,
                Permissions.DELETE_ENVIRONMENT_IN_APPLICATION,
                Permissions.DEACTIVATE_ENVIRONMENT_IN_APPLICATION,
                Permissions.VIEW_ENVIRONMENT_IN_APPLICATION,
                Permissions.RENAME_ENVIRONMENT_IN_APPLICATION,
            ]
        ),
        Role(
            name='developer',
            description='',
            permissions=[
                Permissions.VIEW_USAGE_REPORT,
                Permissions.VIEW_USAGE_DOLLARS,
                Permissions.VIEW_APPLICATION_IN_WORKSPACE,
                Permissions.VIEW_ENVIRONMENT_IN_APPLICATION
            ]
        ),
        Role(
            name='billing_auditor',
            description='',
            permissions=[
                Permissions.VIEW_USAGE_REPORT,
                Permissions.VIEW_USAGE_DOLLARS,

                Permissions.VIEW_APPLICATION_IN_WORKSPACE,

                Permissions.VIEW_ENVIRONMENT_IN_APPLICATION,
            ]
        ),
        Role(
            name='security_auditor',
            description='',
            permissions=[
                Permissions.VIEW_ASSIGNED_ATAT_ROLE_CONFIGURATIONS,
                Permissions.VIEW_ASSIGNED_CSP_ROLE_CONFIGURATIONS,

                Permissions.VIEW_ATAT_PERMISSIONS,

                Permissions.VIEW_APPLICATION_IN_WORKSPACE,

                Permissions.VIEW_ENVIRONMENT_IN_APPLICATION,
            ]
        ),
    ]

    session.add_all(roles)
    session.commit()


def downgrade():
    db = op.get_bind()
    db.execute("""
        DELETE FROM roles
        WHERE name IN (
            'ccpo',
            'owner',
            'admin',
            'developer',
            'billing_auditor',
            'security_auditor'
        );
    """)
