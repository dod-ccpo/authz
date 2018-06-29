from sqlalchemy import Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from authz.database import db
from authz.models.types import Id


class WorkspaceRole(db.Model):
    id = Id()
    workspace_id = db.Column(UUID(as_uuid=True), index=True)
    role_id = db.Column(UUID(as_uuid=True), db.ForeignKey("roles.id"))
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), index=True)
    role = relationship("Role")


Index(
    "workspace_role_user_workspace",
    WorkspaceRole.user_id,
    WorkspaceRole.workspace_id,
    unique=True,
)
