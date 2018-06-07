from sqlalchemy.dialects.postgresql import UUID

from authz.database import db
from authz.models.types import Id


class WorkspaceRole(db.Model):
    id = Id()
    workspace_id = db.Column(UUID(as_uuid=True))
    role_id = db.Column(UUID(as_uuid=True), db.ForeignKey('roles.id'))
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))

