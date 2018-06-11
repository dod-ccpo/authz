import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID

from authz.database import db


def Id():
    return db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("uuid_generate_v4()"))
