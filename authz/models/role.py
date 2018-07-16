from sqlalchemy.dialects.postgresql import ARRAY

from authz.database import db
from authz.models.types import Id


class Role(db.Model):
    __tablename__ = "roles"

    id = Id()
    name = db.Column(db.String, index=True, unique=True)
    description = db.Column(db.String)
    permissions = db.Column(ARRAY(db.String), index=True, server_default="{}")
