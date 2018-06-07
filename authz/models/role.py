from authz.database import db
from sqlalchemy.dialects.postgresql import ARRAY


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    description = db.Column(db.String)
    permissions = db.Column(ARRAY(db.String))
