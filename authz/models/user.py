from sqlalchemy.orm import relationship

from authz.database import db
from authz.models.types import Id

class User(db.Model):
    __tablename__ = 'users'

    id = Id()
    username = db.Column(db.String)
    workspace_roles = relationship('WorkspaceRole', backref='user')
