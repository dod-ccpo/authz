from sqlalchemy.orm.exc import NoResultFound

from authz.database import db
from authz.models import User, WorkspaceRole, Role
from .exceptions import NotFoundError


class WorkspaceUser(object):
    def __init__(self, user, workspace_role):
        self.user = user
        self.workspace_role = workspace_role

    def permissions(self):
        atat_permissions = set(self.user.atat_role.permissions)
        workspace_permissions = (
            [] if self.workspace_role is None else self.workspace_role.role.permissions
        )
        return set(workspace_permissions).union(atat_permissions)

    def workspace_id(self):
        return self.workspace_role.workspace_id


class WorkspaceUsers(object):
    @classmethod
    def get(cls, workspace_id, user_id):
        try:
            user = User.query.filter_by(id=user_id).one()
        except NoResultFound:
            raise NotFoundError("user")

        try:
            workspace_role = (
                WorkspaceRole.query.join(User)
                .filter(User.id == user_id, WorkspaceRole.workspace_id == workspace_id)
                .one()
            )
        except NoResultFound:
            workspace_role = None

        return WorkspaceUser(user, workspace_role)

    @classmethod
    def add_many(cls, workspace_id, workspace_user_dicts):
        workspace_users = []

        for user_dict in workspace_user_dicts:
            try:
                user = User.query.filter_by(id=user_dict["id"]).one()
            except NoResultFound:
                default_role = Role.query.filter_by(name="developer").one_or_none()
                user = User(id=user_dict["id"], atat_role=default_role)

            try:
                role = Role.query.filter_by(name=user_dict["workspace_role"]).one()
            except NoResultFound:
                raise NotFoundError("role")

            new_workspace_role = WorkspaceRole(
                user=user, role_id=role.id, workspace_id=workspace_id
            )
            user.workspace_roles.append(new_workspace_role)

            workspace_user = WorkspaceUser(user, new_workspace_role)
            workspace_users.append(workspace_user)

            db.session.add(user)

        db.session.commit()

        return workspace_users
