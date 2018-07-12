from sqlalchemy.orm.exc import NoResultFound

from authz.models import User, WorkspaceRole
from .exceptions import NotFoundError


class WorkspaceUser(object):

    def __init__(self, user, workspace_role):
        self.user = user
        self.workspace_role = workspace_role

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

        return cls(user, workspace_role)

    def permissions(self):
        atat_permissions = set(self.user.atat_role.permissions)
        workspace_permissions = [] if self.workspace_role is None else self.workspace_role.role.permissions
        return set(workspace_permissions).union(atat_permissions)

    def workspace_id(self):
        return self.workspace_role.workspace_id
