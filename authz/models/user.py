from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from authz.database import db
from authz.models.types import Id


class User(db.Model):
    __tablename__ = "users"

    id = Id()
    username = db.Column(db.String)
    atat_role_id = db.Column(UUID(as_uuid=True), db.ForeignKey("roles.id"))

    atat_role = relationship("Role")
    workspace_roles = relationship("WorkspaceRole", backref="user")

    @property
    def atat_permissions(self):
        return self.atat_role.permissions
